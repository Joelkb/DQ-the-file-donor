<p align="center">
  <img src="https://telegra.ph/file/171925d184de01b3055dc.jpg" alt="DQ-The-File-Donor Logo">
</p>
<h1 align="center">
  <b>DQ-The-File-Donor Bot</b>
</h1>

![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=Welcome+To+DQ-The-File-Donor!;Created+by+Jᴏᴇʟ+ᠰ+TɢX!;A+simple+and+powerful+Bot!;A+Bot+with+double+button!;Start+message+with+pic!;And+more+features!)
</p>

[![Stars](https://img.shields.io/github/stars/Joelkb/DQ-The-File-Donor?style=flat-square&color=yellow)](https://github.com/Joelkb/DQ-The-File-Donor/stargazers)
[![Forks](https://img.shields.io/github/forks/Joelkb/DQ-The-File-Donor?style=flat-square&color=orange)](https://github.com/Joelkb/DQ-The-File-Donor/fork)
[![Size](https://img.shields.io/github/repo-size/Joelkb/DQ-The-File-Donor?style=flat-square&color=green)](https://github.com/Joelkb/DQ-The-File-Donor/)   
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/Joelkb/DQ-The-File-Donor)   
[![Contributors](https://img.shields.io/github/contributors/Joelkb/DQ-The-File-Donor?style=flat-square&color=green)](https://github.com/Joelkb/DQ-The-File-Donor/graphs/contributors)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/Joelkb/DQ-The-File-Donor/blob/main/LICENSE)
[![Sparkline](https://stars.medv.io/Joelkb/DQ-The-File-Donor.svg)](https://stars.medv.io/Joelkb/DQ-The-File-Donor)

## Features
- [x] IMDB Template Set
- [x] Indexes Files above 2GB
- [x] Settings Menu
- [x] Welcome Message
- [x] Automatic File Filtering
- [x] Double Filter Button
- [x] Single Filter Button
- [x] Bot PM File Send Mode
- [x] Auto File Send
- [x] Forward Restriction
- [x] File Protect
- [x] Manual File Filtering
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB search
- [x] Inline Search
- [x] Random pics
- [x] ids and User info 
- [x] Stats
- [x] Users
- [x] Chats
- [x] User Ban
- [x] User Unban
- [x] Chat Leave
- [x] Chat Disable
- [x] Channel
- [x] Spelling Check Feature
- [x] File Store
- [x] Auto Delete
- [x] Heroku Dyno Check
- [x] Bot Uptime
- [x] Bot work day prediction

## Commands
```
• /logs - to get the rescent errors
• /stats - to get status of files in db.
• /connections - To see all connected groups
• /settings - To open settings menu
• /filter - add manual filters
• /filters - view filters
• /connect - connect to PM.
• /disconnect - disconnect from PM
• /del - delete a filter
• /delall - delete all filters
• /deleteall - delete all indexed files.
• /delete - delete a specific file from index.
• /info - get user info
• /id - get tg ids.
• /imdb - fetch info from imdb.
• /search - To search from various sources
• /start - To start the bot
• /setskip - To skip number of messages when indexing files
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids 
• /leave  - to leave from a chat.
• /disable  -  do disable a chat.
• /enable - re-enable chat.
• /ban  - to ban a user.
• /unban  - to unban a user.
• /channel - to get list of total connected channels
• /broadcast - to broadcast a message to all Eva Maria users
• /batch - to create link for multiple posts
• /link - to create link for one post
• /status - Your Heroku API Key to check dyno, bot uptime and bot working day prediction.
• /set_template - To set a custom IMDb template for individual groups
```

## Variables

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
* `HEROKU_API_KEY`: Your Heroku API Key to check dyno, bot uptime and bot working day prediction
### Optional Variables
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used separated by space )
* `FILE_STORE_CHANNEL`: Channel from were file store links of posts should be made.Separate multiple IDs by space
* Check [info.py](https://github.com/Joelkb/DQ-The-File-Donor/blob/master/info.py) for more optional variables


<details><summary>Deploy To Heroku</summary>
<p>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/Joelkb/DQ-the-file-donor">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy To Heroku">
</a>
</p>
</details>
<details><summary>Deploy To Heroku Via Bot</summary>
<p>
<br>
<a href="https://telegram.dog/XTZ_HerokuBot?start=Sm9lbGtiL0RRLXRoZS1maWxlLWRvbm9yIG1hc3Rlcg">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy Via Heroku Bot">
</a>
</p>
</details>
<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone https://github.com/Joelkb/DQ-The-File-Donor
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>

<hr>

## Credits 
* [![EvaMaria-Devs](https://img.shields.io/static/v1?label=EvaMaria&message=devs&color=critical)](https://telegram.dog/EvaMariaDevs)
* [![Joel-TGX](https://img.shields.io/static/v1?label=JoelTGX&message=Github&color=critical)](https://github.com/Joelkb)
* [![Contact](https://img.shields.io/static/v1?label=Contact&message=OnTelegram&color=critical)](https://telegram.me/creatorbeatz)

## Thanks to 
 - Thanks To Dan For His Awesome [Library](https://github.com/pyrogram/pyrogram)
 - Thanks To Mahesh For His Awesome [Media-Search-bot](https://github.com/Mahesh0253/Media-Search-bot)
 - Thanks To [Trojanz](https://github.com/trojanzhex) for Their Awesome [Unlimited Filter Bot](https://github.com/TroJanzHEX/Unlimited-Filter-Bot) And [AutoFilterBoT](https://github.com/trojanzhex/auto-filter-bot)
 - Thanks To All Everyone In This Journey
 - Thanks To [EvamariaTG](https://raw.githubusercontent.com/EvamariaTG) for their awesome [EvaMaria Bot](https://raw.githubusercontent.com/EvamariaTG/EvaMaria)
 - Thanks To Me 😂

## Disclaimer
[![GNU Affero General Public License 2.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)    
Licensed under [GNU AGPL 2.0.](https://github.com/Joelkb/DQ-The-File-Donor/blob/master/LICENSE)
Selling The Codes To Other People For Money Is *Strictly Prohibited*.

