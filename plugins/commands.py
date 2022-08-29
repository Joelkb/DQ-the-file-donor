import os
import logging
import random
import asyncio
from Script import script
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, LOG_CHANNEL, PICS, BATCH_FILE_CAPTION, CUSTOM_FILE_CAPTION, PROTECT_CONTENT
from utils import get_settings, get_size, is_subscribed, save_group_settings, temp
from database.connections_mdb import active_connection
import re
import json
import base64
logger = logging.getLogger(__name__)

BATCH_FILES = {}

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        buttons = [[
                    InlineKeyboardButton('⤬ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ⤬', url=f'https://t.me/auto_m4_mallumovies_bot?startgroup=true')
                ],[
                    InlineKeyboardButton('♚ Bᴏᴛ Oᴡɴᴇʀ', callback_data="owner_info"),
                    InlineKeyboardButton('⌬ Mᴏᴠɪᴇ Gʀᴏᴜᴘ', url='https://t.me/filmy_harbour')
                ],[
                    InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),
                    InlineKeyboardButton('⍟ Aʙᴏᴜᴛ', callback_data='about')
                ],[
                    InlineKeyboardButton('✇ Jᴏɪɴ Oᴜʀ Mᴀɪɴ Cʜᴀɴɴᴇʟ ✇', url='https://t.me/+LJRsBp82HiJhNDhl')
                  ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
        await asyncio.sleep(2) # 😢 https://github.com/EvamariaTG/EvaMaria/blob/master/plugins/p_ttishow.py#L17 😬 wait a bit, before checking.
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        buttons = [[
                    InlineKeyboardButton('⤬ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ⤬', url=f'https://t.me/auto_m4_mallumovies_bot?startgroup=true')
                ],[
                    InlineKeyboardButton('♚ Bᴏᴛ Oᴡɴᴇʀ', callback_data="owner_info"),
                    InlineKeyboardButton('⌬ Mᴏᴠɪᴇ Gʀᴏᴜᴘ', url='https://t.me/filmy_harbour')
                ],[
                    InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),
                    InlineKeyboardButton('⍟ Aʙᴏᴜᴛ', callback_data='about')
                ],[
                    InlineKeyboardButton('✇ Jᴏɪɴ Oᴜʀ Mᴀɪɴ Cʜᴀɴɴᴇʟ ✇', url='https://t.me/+LJRsBp82HiJhNDhl')
                  ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return
    if AUTH_CHANNEL and not await is_subscribed(client, message):
        try:
            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        except ChatAdminRequired:
            logger.error("Make sure Bot is admin in Forcesub channel")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "❆ Jᴏɪɴ Oᴜʀ Bᴀᴄᴋ-Uᴘ Cʜᴀɴɴᴇʟ ❆", url=invite_link.invite_link
                )
            ]
        ]

        if message.command[1] != "subscribe":
            try:
                kk, file_id = message.command[1].split("_", 1)
                pre = 'checksubp' if kk == 'filep' else 'checksub' 
                btn.append([InlineKeyboardButton("↻ Tʀʏ Aɢᴀɪɴ", callback_data=f"{pre}#{file_id}")])
            except (IndexError, ValueError):
                btn.append([InlineKeyboardButton("↻ Tʀʏ Aɢᴀɪɴ", url=f"https://t.me/{temp.U_NAME}?start={message.command[1]}")])
        await client.send_message(
            chat_id=message.from_user.id,
            text="**You are not in our Back-up channel given below so you don't get the movie file...\n\nIf you want the movie file, click on the '🍿ᴊᴏɪɴ ᴏᴜʀ ʙᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ🍿' button below and join our back-up channel, then click on the '🔄 Try Again' button below...\n\nThen you will get the movie files...**",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode=enums.ParseMode.MARKDOWN
            )
        return
    if len(message.command) == 2 and message.command[1] in ["subscribe", "error", "okay", "help"]:
        buttons = [[
                    InlineKeyboardButton('⤬ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ⤬', url=f'https://t.me/auto_m4_mallumovies_bot?startgroup=true')
                ],[
                    InlineKeyboardButton('♚ Bᴏᴛ Oᴡɴᴇʀ', callback_data="owner_info"),
                    InlineKeyboardButton('⌬ Mᴏᴠɪᴇ Gʀᴏᴜᴘ', url='https://t.me/filmy_harbour')
                ],[
                    InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),
                    InlineKeyboardButton('⍟ Aʙᴏᴜᴛ', callback_data='about')
                ],[
                    InlineKeyboardButton('✇ Jᴏɪɴ Oᴜʀ Mᴀɪɴ Cʜᴀɴɴᴇʟ ✇', url='https://t.me/+LJRsBp82HiJhNDhl')
                  ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return
    data = message.command[1]
    try:
        pre, file_id = data.split('_', 1)
    except:
        file_id = data
        pre = ""
    if data.split("-", 1)[0] == "BATCH":
        sts = await message.reply("<b>Please wait...</b>")
        file_id = data.split("-", 1)[1]
        msgs = BATCH_FILES.get(file_id)
        if not msgs:
            file = await client.download_media(file_id)
            try: 
                with open(file) as file_data:
                    msgs=json.loads(file_data.read())
            except:
                await sts.edit("FAILED")
                return await client.send_message(LOG_CHANNEL, "UNABLE TO OPEN FILE.")
            os.remove(file)
            BATCH_FILES[file_id] = msgs
        for msg in msgs:
            title = msg.get("title")
            size=get_size(int(msg.get("size", 0)))
            f_caption=msg.get("caption", "")
            if BATCH_FILE_CAPTION:
                try:
                    f_caption=BATCH_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
                except Exception as e:
                    logger.exception(e)
                    f_caption=f_caption
            if f_caption is None:
                f_caption = f"{title}"
            try:
                await client.send_cached_media(
                    chat_id=message.from_user.id,
                    file_id=msg.get("file_id"),
                    caption=f_caption,
                    protect_content=msg.get('protect', False),
                    reply_markup=InlineKeyboardMarkup(
                        [
                         [
                          InlineKeyboardButton("⚡ Jᴏɪɴ Gʀᴏᴜᴘ ⚡", url="https://t.me/filmy_harbour"),
                          InlineKeyboardButton("💥 Sʜᴀʀᴇ 💥", url="https://t.me/share/url?url=%F0%9F%A4%A9%20%D2%93%C9%AA%CA%9F%E1%B4%8D%CA%8F%20%CA%9C%E1%B4%80%CA%80%CA%99%E1%B4%8F%E1%B4%9C%CA%80%20%F0%9F%A4%A9%0A%0A%C2%BB%20%E1%B4%8F%C9%B4%20%E1%B4%9B%CA%9C%E1%B4%87%20s%E1%B4%98%E1%B4%8F%E1%B4%9B%20%CA%80%E1%B4%87s%E1%B4%98%E1%B4%8F%C9%B4s%E1%B4%87.%0A%C2%BB%20%F0%9D%9F%B8%F0%9D%9F%BAx%F0%9D%9F%BD%20%E1%B4%8F%C9%B4%CA%9F%C9%AA%C9%B4%E1%B4%87.%0A%C2%BB%20%E1%B4%A1%C9%AA%E1%B4%85%E1%B4%87%20%E1%B4%A0%E1%B4%80%CA%80%C9%AA%E1%B4%87%E1%B4%9B%CA%8F%20%E1%B4%8F%D2%93%20%E1%B4%8F%CA%9F%E1%B4%85%20%E1%B4%80%C9%B4%E1%B4%85%20%C9%B4%E1%B4%87%E1%B4%A1%20%E1%B4%8D%E1%B4%8F%E1%B4%A0%C9%AA%E1%B4%87%20%E1%B4%84%E1%B4%8F%CA%9F%CA%9F%E1%B4%87%E1%B4%84%E1%B4%9B%C9%AA%E1%B4%8F%C9%B4s%20%C9%AA%C9%B4%20%E1%B4%80%CA%9F%CA%9F%20%CA%9F%E1%B4%80%C9%B4%C9%A2%E1%B4%9C%E1%B4%80%C9%A2%E1%B4%87s.%0A%C2%BB%20%E1%B4%80%E1%B4%85%E1%B4%8D%C9%AA%C9%B4%20s%E1%B4%9C%E1%B4%98%E1%B4%98%E1%B4%8F%CA%80%E1%B4%9B.%0A%C2%BB%20%F0%9D%9F%BF.%F0%9D%9F%BB%20%CA%9F%E1%B4%80%E1%B4%8B%CA%9C%2B%20%E1%B4%8D%E1%B4%8F%E1%B4%A0%C9%AA%E1%B4%87%20%E1%B4%80%C9%B4%E1%B4%85%20s%E1%B4%87%CA%80%C9%AA%E1%B4%87s%20%D2%93%C9%AA%CA%9F%E1%B4%87s.%0A%0A%E2%98%85%20%E1%B4%8A%E1%B4%8F%C9%AA%C9%B4%20%C9%B4%E1%B4%8F%E1%B4%A1%20%E2%98%85%0A%40filmy_harbour%0A%40filmy_harbour%0A%40filmy_harbour%0A%0A%E2%98%85%20s%CA%9C%E1%B4%80%CA%80%E1%B4%87%20%E1%B4%9B%CA%9C%C9%AAs%20%E1%B4%8D%E1%B4%87ss%E1%B4%80%C9%A2%E1%B4%87%20%E1%B4%9B%E1%B4%8F%20%CA%8F%E1%B4%8F%E1%B4%9C%CA%80%20%D2%93%CA%80%C9%AA%E1%B4%87%C9%B4%E1%B4%85s%20%E2%98%85")
                       ],[
                          InlineKeyboardButton("🔖 Dᴏᴡɴʟᴏᴀᴅ Sᴜʙᴛɪᴛʟᴇ 🔖", url="https://telegra.ph/DOWNLOAD-SUBTITLES-01-05")
                         ]
                        ]
                    )
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
                logger.warning(f"Floodwait of {e.x} sec.")
                await client.send_cached_media(
                    chat_id=message.from_user.id,
                    file_id=msg.get("file_id"),
                    caption=f_caption,
                    protect_content=msg.get('protect', False),
                    reply_markup=InlineKeyboardMarkup(
                        [
                         [
                          InlineKeyboardButton("⚡ Jᴏɪɴ Gʀᴏᴜᴘ ⚡", url="https://t.me/filmy_harbour"),
                          InlineKeyboardButton("💥 Sʜᴀʀᴇ 💥", url="https://t.me/share/url?url=%F0%9F%A4%A9%20%D2%93%C9%AA%CA%9F%E1%B4%8D%CA%8F%20%CA%9C%E1%B4%80%CA%80%CA%99%E1%B4%8F%E1%B4%9C%CA%80%20%F0%9F%A4%A9%0A%0A%C2%BB%20%E1%B4%8F%C9%B4%20%E1%B4%9B%CA%9C%E1%B4%87%20s%E1%B4%98%E1%B4%8F%E1%B4%9B%20%CA%80%E1%B4%87s%E1%B4%98%E1%B4%8F%C9%B4s%E1%B4%87.%0A%C2%BB%20%F0%9D%9F%B8%F0%9D%9F%BAx%F0%9D%9F%BD%20%E1%B4%8F%C9%B4%CA%9F%C9%AA%C9%B4%E1%B4%87.%0A%C2%BB%20%E1%B4%A1%C9%AA%E1%B4%85%E1%B4%87%20%E1%B4%A0%E1%B4%80%CA%80%C9%AA%E1%B4%87%E1%B4%9B%CA%8F%20%E1%B4%8F%D2%93%20%E1%B4%8F%CA%9F%E1%B4%85%20%E1%B4%80%C9%B4%E1%B4%85%20%C9%B4%E1%B4%87%E1%B4%A1%20%E1%B4%8D%E1%B4%8F%E1%B4%A0%C9%AA%E1%B4%87%20%E1%B4%84%E1%B4%8F%CA%9F%CA%9F%E1%B4%87%E1%B4%84%E1%B4%9B%C9%AA%E1%B4%8F%C9%B4s%20%C9%AA%C9%B4%20%E1%B4%80%CA%9F%CA%9F%20%CA%9F%E1%B4%80%C9%B4%C9%A2%E1%B4%9C%E1%B4%80%C9%A2%E1%B4%87s.%0A%C2%BB%20%E1%B4%80%E1%B4%85%E1%B4%8D%C9%AA%C9%B4%20s%E1%B4%9C%E1%B4%98%E1%B4%98%E1%B4%8F%CA%80%E1%B4%9B.%0A%C2%BB%20%F0%9D%9F%BF.%F0%9D%9F%BB%20%CA%9F%E1%B4%80%E1%B4%8B%CA%9C%2B%20%E1%B4%8D%E1%B4%8F%E1%B4%A0%C9%AA%E1%B4%87%20%E1%B4%80%C9%B4%E1%B4%85%20s%E1%B4%87%CA%80%C9%AA%E1%B4%87s%20%D2%93%C9%AA%CA%9F%E1%B4%87s.%0A%0A%E2%98%85%20%E1%B4%8A%E1%B4%8F%C9%AA%C9%B4%20%C9%B4%E1%B4%8F%E1%B4%A1%20%E2%98%85%0A%40filmy_harbour%0A%40filmy_harbour%0A%40filmy_harbour%0A%0A%E2%98%85%20s%CA%9C%E1%B4%80%CA%80%E1%B4%87%20%E1%B4%9B%CA%9C%C9%AAs%20%E1%B4%8D%E1%B4%87ss%E1%B4%80%C9%A2%E1%B4%87%20%E1%B4%9B%E1%B4%8F%20%CA%8F%E1%B4%8F%E1%B4%9C%CA%80%20%D2%93%CA%80%C9%AA%E1%B4%87%C9%B4%E1%B4%85s%20%E2%98%85")
                       ],[
                          InlineKeyboardButton("🔖 Dᴏᴡɴʟᴏᴀᴅ Sᴜʙᴛɪᴛʟᴇ 🔖", url="https://telegra.ph/DOWNLOAD-SUBTITLES-01-05")
                         ]
                        ]
                    )
                )
            except Exception as e:
                logger.warning(e, exc_info=True)
                continue
            await asyncio.sleep(1) 
        await sts.delete()
        return
    elif data.split("-", 1)[0] == "DSTORE":
        sts = await message.reply("<b>Please wait...</b>")
        b_string = data.split("-", 1)[1]
        decoded = (base64.urlsafe_b64decode(b_string + "=" * (-len(b_string) % 4))).decode("ascii")
        try:
            f_msg_id, l_msg_id, f_chat_id, protect = decoded.split("_", 3)
        except:
            f_msg_id, l_msg_id, f_chat_id = decoded.split("_", 2)
            protect = "/pbatch" if PROTECT_CONTENT else "batch"
        diff = int(l_msg_id) - int(f_msg_id)
        async for msg in client.iter_messages(int(f_chat_id), int(l_msg_id), int(f_msg_id)):
            if msg.media:
                media = getattr(msg, msg.media.value)
                if BATCH_FILE_CAPTION:
                    try:
                        f_caption=BATCH_FILE_CAPTION.format(file_name=getattr(media, 'file_name', ''), file_size=getattr(media, 'file_size', ''), file_caption=getattr(msg, 'caption', ''))
                    except Exception as e:
                        logger.exception(e)
                        f_caption = getattr(msg, 'caption', '')
                else:
                    media = getattr(msg, msg.media.value)
                    file_name = getattr(media, 'file_name', '')
                    f_caption = getattr(msg, 'caption', file_name)
                try:
                    await msg.copy(message.chat.id, caption=f_caption, protect_content=True if protect == "/pbatch" else False)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await msg.copy(message.chat.id, caption=f_caption, protect_content=True if protect == "/pbatch" else False)
                except Exception as e:
                    logger.exception(e)
                    continue
            elif msg.empty:
                continue
            else:
                try:
                    await msg.copy(message.chat.id, protect_content=True if protect == "/pbatch" else False)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await msg.copy(message.chat.id, protect_content=True if protect == "/pbatch" else False)
                except Exception as e:
                    logger.exception(e)
                    continue
            await asyncio.sleep(1) 
        return await sts.delete()
        

    files_ = await get_file_details(file_id)           
    if not files_:
        pre, file_id = ((base64.urlsafe_b64decode(data + "=" * (-len(data) % 4))).decode("ascii")).split("_", 1)
        try:
            msg = await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=file_id,
                protect_content=True if pre == 'filep' else False,
                reply_markup=InlineKeyboardMarkup(
                    [
                     [
                      InlineKeyboardButton("⚡ Jᴏɪɴ Gʀᴏᴜᴘ ⚡", url="https://t.me/filmy_harbour"),
                      InlineKeyboardButton("💥 Sʜᴀʀᴇ 💥", url="https://t.me/share/url?url=%F0%9F%A4%A9%20%D2%93%C9%AA%CA%9F%E1%B4%8D%CA%8F%20%CA%9C%E1%B4%80%CA%80%CA%99%E1%B4%8F%E1%B4%9C%CA%80%20%F0%9F%A4%A9%0A%0A%C2%BB%20%E1%B4%8F%C9%B4%20%E1%B4%9B%CA%9C%E1%B4%87%20s%E1%B4%98%E1%B4%8F%E1%B4%9B%20%CA%80%E1%B4%87s%E1%B4%98%E1%B4%8F%C9%B4s%E1%B4%87.%0A%C2%BB%20%F0%9D%9F%B8%F0%9D%9F%BAx%F0%9D%9F%BD%20%E1%B4%8F%C9%B4%CA%9F%C9%AA%C9%B4%E1%B4%87.%0A%C2%BB%20%E1%B4%A1%C9%AA%E1%B4%85%E1%B4%87%20%E1%B4%A0%E1%B4%80%CA%80%C9%AA%E1%B4%87%E1%B4%9B%CA%8F%20%E1%B4%8F%D2%93%20%E1%B4%8F%CA%9F%E1%B4%85%20%E1%B4%80%C9%B4%E1%B4%85%20%C9%B4%E1%B4%87%E1%B4%A1%20%E1%B4%8D%E1%B4%8F%E1%B4%A0%C9%AA%E1%B4%87%20%E1%B4%84%E1%B4%8F%CA%9F%CA%9F%E1%B4%87%E1%B4%84%E1%B4%9B%C9%AA%E1%B4%8F%C9%B4s%20%C9%AA%C9%B4%20%E1%B4%80%CA%9F%CA%9F%20%CA%9F%E1%B4%80%C9%B4%C9%A2%E1%B4%9C%E1%B4%80%C9%A2%E1%B4%87s.%0A%C2%BB%20%E1%B4%80%E1%B4%85%E1%B4%8D%C9%AA%C9%B4%20s%E1%B4%9C%E1%B4%98%E1%B4%98%E1%B4%8F%CA%80%E1%B4%9B.%0A%C2%BB%20%F0%9D%9F%BF.%F0%9D%9F%BB%20%CA%9F%E1%B4%80%E1%B4%8B%CA%9C%2B%20%E1%B4%8D%E1%B4%8F%E1%B4%A0%C9%AA%E1%B4%87%20%E1%B4%80%C9%B4%E1%B4%85%20s%E1%B4%87%CA%80%C9%AA%E1%B4%87s%20%D2%93%C9%AA%CA%9F%E1%B4%87s.%0A%0A%E2%98%85%20%E1%B4%8A%E1%B4%8F%C9%AA%C9%B4%20%C9%B4%E1%B4%8F%E1%B4%A1%20%E2%98%85%0A%40filmy_harbour%0A%40filmy_harbour%0A%40filmy_harbour%0A%0A%E2%98%85%20s%CA%9C%E1%B4%80%CA%80%E1%B4%87%20%E1%B4%9B%CA%9C%C9%AAs%20%E1%B4%8D%E1%B4%87ss%E1%B4%80%C9%A2%E1%B4%87%20%E1%B4%9B%E1%B4%8F%20%CA%8F%E1%B4%8F%E1%B4%9C%CA%80%20%D2%93%CA%80%C9%AA%E1%B4%87%C9%B4%E1%B4%85s%20%E2%98%85")
                   ],[
                      InlineKeyboardButton("🔖 Dᴏᴡɴʟᴏᴀᴅ Sᴜʙᴛɪᴛʟᴇ 🔖", url="https://telegra.ph/DOWNLOAD-SUBTITLES-01-05")
                     ]
                    ]
                )
            )
            filetype = msg.media
            file = getattr(msg, filetype.value)
            title = file.file_name
            size=get_size(file.file_size)
            f_caption = f"<code>{title}</code>"
            if CUSTOM_FILE_CAPTION:
                try:
                    f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='')
                except:
                    return
            await msg.edit_caption(f_caption)
            return
        except:
            pass
        return await message.reply('No such file exist.')
    files = files_[0]
    title = files.file_name
    size=get_size(files.file_size)
    f_caption=files.caption
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
        except Exception as e:
            logger.exception(e)
            f_caption=f_caption
    if f_caption is None:
        f_caption = f"{files.file_name}"
    await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        protect_content=True if pre == 'filep' else False,
        reply_markup=InlineKeyboardMarkup(
            [
             [
              InlineKeyboardButton("⚡ Jᴏɪɴ Gʀᴏᴜᴘ ⚡", url="https://t.me/filmy_harbour"),
              InlineKeyboardButton("💥 Sʜᴀʀᴇ 💥", url="https://t.me/share/url?url=%F0%9F%A4%A9%20%D2%93%C9%AA%CA%9F%E1%B4%8D%CA%8F%20%CA%9C%E1%B4%80%CA%80%CA%99%E1%B4%8F%E1%B4%9C%CA%80%20%F0%9F%A4%A9%0A%0A%C2%BB%20%E1%B4%8F%C9%B4%20%E1%B4%9B%CA%9C%E1%B4%87%20s%E1%B4%98%E1%B4%8F%E1%B4%9B%20%CA%80%E1%B4%87s%E1%B4%98%E1%B4%8F%C9%B4s%E1%B4%87.%0A%C2%BB%20%F0%9D%9F%B8%F0%9D%9F%BAx%F0%9D%9F%BD%20%E1%B4%8F%C9%B4%CA%9F%C9%AA%C9%B4%E1%B4%87.%0A%C2%BB%20%E1%B4%A1%C9%AA%E1%B4%85%E1%B4%87%20%E1%B4%A0%E1%B4%80%CA%80%C9%AA%E1%B4%87%E1%B4%9B%CA%8F%20%E1%B4%8F%D2%93%20%E1%B4%8F%CA%9F%E1%B4%85%20%E1%B4%80%C9%B4%E1%B4%85%20%C9%B4%E1%B4%87%E1%B4%A1%20%E1%B4%8D%E1%B4%8F%E1%B4%A0%C9%AA%E1%B4%87%20%E1%B4%84%E1%B4%8F%CA%9F%CA%9F%E1%B4%87%E1%B4%84%E1%B4%9B%C9%AA%E1%B4%8F%C9%B4s%20%C9%AA%C9%B4%20%E1%B4%80%CA%9F%CA%9F%20%CA%9F%E1%B4%80%C9%B4%C9%A2%E1%B4%9C%E1%B4%80%C9%A2%E1%B4%87s.%0A%C2%BB%20%E1%B4%80%E1%B4%85%E1%B4%8D%C9%AA%C9%B4%20s%E1%B4%9C%E1%B4%98%E1%B4%98%E1%B4%8F%CA%80%E1%B4%9B.%0A%C2%BB%20%F0%9D%9F%BF.%F0%9D%9F%BB%20%CA%9F%E1%B4%80%E1%B4%8B%CA%9C%2B%20%E1%B4%8D%E1%B4%8F%E1%B4%A0%C9%AA%E1%B4%87%20%E1%B4%80%C9%B4%E1%B4%85%20s%E1%B4%87%CA%80%C9%AA%E1%B4%87s%20%D2%93%C9%AA%CA%9F%E1%B4%87s.%0A%0A%E2%98%85%20%E1%B4%8A%E1%B4%8F%C9%AA%C9%B4%20%C9%B4%E1%B4%8F%E1%B4%A1%20%E2%98%85%0A%40filmy_harbour%0A%40filmy_harbour%0A%40filmy_harbour%0A%0A%E2%98%85%20s%CA%9C%E1%B4%80%CA%80%E1%B4%87%20%E1%B4%9B%CA%9C%C9%AAs%20%E1%B4%8D%E1%B4%87ss%E1%B4%80%C9%A2%E1%B4%87%20%E1%B4%9B%E1%B4%8F%20%CA%8F%E1%B4%8F%E1%B4%9C%CA%80%20%D2%93%CA%80%C9%AA%E1%B4%87%C9%B4%E1%B4%85s%20%E2%98%85")
           ],[
              InlineKeyboardButton("🔖 Dᴏᴡɴʟᴏᴀᴅ Sᴜʙᴛɪᴛʟᴇ 🔖", url="https://telegra.ph/DOWNLOAD-SUBTITLES-01-05")
             ]
            ]
        )
    )
                    

@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
           
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))

@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return
    
    file_id, file_ref = unpack_new_file_id(media.file_id)

    result = await Media.collection.delete_one({
        '_id': file_id,
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))
        result = await Media.collection.delete_many({
            'file_name': file_name,
            'file_size': media.file_size,
            'mime_type': media.mime_type
            })
        if result.deleted_count:
            await msg.edit('File is successfully deleted from database')
        else:
            # files indexed before https://github.com/EvamariaTG/EvaMaria/commit/f3d2a1bcb155faf44178e5d7a685a1b533e714bf#diff-86b613edf1748372103e94cacff3b578b36b698ef9c16817bb98fe9ef22fb669R39 
            # have original file name.
            result = await Media.collection.delete_many({
                'file_name': media.file_name,
                'file_size': media.file_size,
                'mime_type': media.mime_type
            })
            if result.deleted_count:
                await msg.edit('File is successfully deleted from database')
            else:
                await msg.edit('File not found in database')


@Client.on_message(filters.command('deleteall') & filters.user(ADMINS))
async def delete_all_index(bot, message):
    await message.reply_text(
        'This will delete all indexed files.\nDo you want to continue??',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="YES", callback_data="autofilter_delete"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="CANCEL", callback_data="close_data"
                    )
                ],
            ]
        ),
        quote=True,
    )


@Client.on_callback_query(filters.regex(r'^autofilter_delete'))
async def delete_all_index_confirm(bot, message):
    await Media.collection.drop()
    await message.answer('Piracy Is Crime')
    await message.message.edit('Succesfully Deleted All The Indexed Files.')


@Client.on_message(filters.command('settings'))
async def settings(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"You are anonymous admin. Use /connect {message.chat.id} in PM")
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("Make sure I'm present in your group!!", quote=True)
                return
        else:
            await message.reply_text("I'm not connected to any groups!", quote=True)
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    st = await client.get_chat_member(grp_id, userid)
    if (
            st.status != enums.ChatMemberStatus.ADMINISTRATOR
            and st.status != enums.ChatMemberStatus.OWNER
            and str(userid) not in ADMINS
    ):
        return

    settings = await get_settings(grp_id)

    if settings is not None:
        buttons = [
            [
                InlineKeyboardButton(
                    'Fɪʟᴛᴇʀ Bᴜᴛᴛᴏɴ',
                    callback_data=f'setgs#button#{settings["button"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    'Sɪɴɢʟᴇ' if settings["button"] else 'Dᴏᴜʙʟᴇ',
                    callback_data=f'setgs#button#{settings["button"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Fɪʟᴇ Sᴇɴᴅ Mᴏᴅᴇ',
                    callback_data=f'setgs#botpm#{settings["botpm"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    'Mᴀɴᴜᴀʟ Sᴛᴀʀᴛ' if settings["botpm"] else 'Aᴜᴛᴏ Sᴇɴᴅ',
                    callback_data=f'setgs#botpm#{settings["botpm"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Fɪʟᴇ Sᴇᴄᴜʀᴇ',
                    callback_data=f'setgs#file_secure#{settings["file_secure"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ Oɴ' if settings["file_secure"] else '✘ Oғғ',
                    callback_data=f'setgs#file_secure#{settings["file_secure"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Iᴍᴅʙ',
                    callback_data=f'setgs#imdb#{settings["imdb"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ Oɴ' if settings["imdb"] else '✘ Oғғ',
                    callback_data=f'setgs#imdb#{settings["imdb"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Sᴘᴇʟʟ Cʜᴇᴄᴋ',
                    callback_data=f'setgs#spell_check#{settings["spell_check"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ Oɴ' if settings["spell_check"] else '✘ Oғғ',
                    callback_data=f'setgs#spell_check#{settings["spell_check"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Wᴇʟᴄᴏᴍᴇ Msɢ',
                    callback_data=f'setgs#welcome#{settings["welcome"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ Oɴ' if settings["welcome"] else '✘ Oғғ',
                    callback_data=f'setgs#welcome#{settings["welcome"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Aᴜᴛᴏ-Dᴇʟᴇᴛᴇ',
                    callback_data=f'setgs#auto_delete#{settings["auto_delete"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '10 Mɪɴs' if settings["auto_delete"] else '✘ Oғғ',
                    callback_data=f'setgs#auto_delete#{settings["auto_delete"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Aᴜᴛᴏ-Fɪʟᴛᴇʀ',
                    callback_data=f'setgs#auto_ffilter#{settings["auto_ffilter"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ Oɴ' if settings["auto_ffilter"] else '✘ Oғғ',
                    callback_data=f'setgs#auto_ffilter#{settings["auto_ffilter"]}#{grp_id}',
                ),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(buttons)

        await message.reply_text(
            text=f"<b>Cʜᴀɴɢᴇ Yᴏᴜʀ Sᴇᴛᴛɪɴɢs Fᴏʀ {title} As Yᴏᴜʀ Wɪsʜ ⚙</b>",
            reply_markup=reply_markup,
            disable_web_page_preview=True,
            parse_mode=enums.ParseMode.HTML,
            reply_to_message_id=message.id
        )



@Client.on_message(filters.command('set_template'))
async def save_template(client, message):
    sts = await message.reply("Checking template")
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"You are anonymous admin. Use /connect {message.chat.id} in PM")
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("Make sure I'm present in your group!!", quote=True)
                return
        else:
            await message.reply_text("I'm not connected to any groups!", quote=True)
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    st = await client.get_chat_member(grp_id, userid)
    if (
            st.status != enums.ChatMemberStatus.ADMINISTRATOR
            and st.status != enums.ChatMemberStatus.OWNER
            and str(userid) not in ADMINS
    ):
        return

    if len(message.command) < 2:
        return await sts.edit("No Input!!")
    template = message.text.split(" ", 1)[1]
    await save_group_settings(grp_id, 'template', template)
    await sts.edit(f"Successfully changed template for {title} to\n\n{template}")
