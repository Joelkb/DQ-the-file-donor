class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ {},
Mʏ Nᴀᴍᴇ Is <a href=https://t.me/{}>{}</a>, I Cᴀɴ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs, Jᴜsᴛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Eɴᴊᴏʏ 😍</b>"""

    HERO = """<b>Hᴇʏ {}
ನಿಮ್ಮ ನೆಚ್ಚಿನ ನಾಯಕನ ಆಯ್ಕೆ ಮಾಡಿ.</b>"""

    HERO1 = """<b>HEY: {}
ನಿಮ್ಮ ನೆಚ್ಚಿನ ನಾಯಕನ ಆಯ್ಕೆ ಮಾಡಿ.</b>"""

    PUNITHRAJKUMAR = """<b>ಪವರ್ ಸ್ಟಾರ್ ಪುನೀತ್ ರಾಜ್‌ಕುಮಾರ್</b>
<code>appu 2002</code>
<code>abhi 2003</code>
<code>maurya 2004</code>
<code>aakash 2005</code>
<code>namma basava 2005</code>
<code>ajay 2006</code>
<code>arasu 2006</code>
<code>milana</code>2007
<code>bindaas 2008</code>
<code>vamshi 2008</code>
<code>raaj the show man 2009</code>
<code>raam</code>2009
<code>prithvi 2010</code>
<code>jackie 2010</code>
<code>hudugaru 2011</code>
<code>paramathma 2011</code>
<code>anna bond 2012</code>
<code>yaare koogadali 2012</code>
<code>ninnindale 2014</code>
<code>power 2014</code>
<code>mythri 2015</code>
<code>rana vikrama 2015</code>
<code>chakravyuha 2016</code>
<code>Doddmane hudga 2016</code>
<code>raajakumara 2017</code>
<code>anjaniputra 2017</code>
<code>natasaarvabhowma 2019</code>
<code>yuvaratna 2021</code>
<code>James 2022</code>
<code>Gandhada Gudi 2022</code>"""

    SHANKARNAG = """<b>ಕರಾಟೆ ಕಿಂಗ್ ಶಂಕರ್ ನಾಗ್</b>
<code>Ondanondu Kaladalli 1978</code>
<code>I Love You 1979</code>
<code>Preethi Madu Thamashe Nodu 1979</code>
<code>Seetharamu 1979</code>
<code>Madhu Chandra 1979</code>
<code>Minchina Ota 1980</code>
<code>Auto Raja 1980</code>
<code>Haddina Kannu 1980</code>
<code>Ondu Hennu Aaru Kannu 1980</code>
<code>Moogana Sedu 1980</code>
<code>Aarada Gaaya 1980</code>
<code>Rusthum Jodi 1980</code>
<code>Janma Janmada Anubandha 1980</code>
<code>Kula Puthra 1981</code>
<code>Hanabalavo Janabalavo 1981</code>
<code>Geetha 1981</code>
<code>Devara Aata 1981</code>
<code>Bhaari Bharjari Bete 1981</code>
<code>Muniyana Madari 1981</code>
<code>Jeevakke Jeeva 1981</code>
<code>Archana 1982</code>
<code>Benki Chendu 1982</code>
<code>Karmika Kallanalla 1982</code>
<code>Nyaya Ellide 1982</code>
<code>Dharma Daari Tappithu 1982</code>
<code>Gedda Maga 1983</code>
<code>Chandi Chamundi 1983</code>
<code>Keralida Hennu 1983</code>
<code>Nyaya Gedditu 1983</code>
<code>Swargadalli Maduve 1983</code>
<code>Aakrosha 1983</code>
<code>Nodi Swamy Navirodu Hige 1983</code>
<code>Raktha Thilaka 1984</code>
<code>Nagabekamma Nagabeku 1984</code>
<code>Gandu Bherunda 1984</code>
<code>Benki Birugali 1984</code>
<code>Thaliya Bhagya 1984</code>
<code>Kalinga Sarpa 1984</code>
<code>Bedaru Bombe 1984</code>
<code>Indina Bharatha 1984</code>
<code>Shapatha 1984</code>
<code>Accident 1984</code>
<code>Pavithra Prema 1984</code>
<code>Aasha Kirana 1984</code>
<code>Utsav 1984</code>
<code>Makkaliralavva Mane Thumba 1984</code>
<code>Apoorva Sangama 1985</code>
<code>Thayi Kanasu 1985</code>
<code>Manava Danava 1985</code>"""

    SHANKARNAG1 = """<code>Kiladi Aliya 1985</code>
<code>Vajra Mushti 1985</code>
<code>Kari Naga 1985</code>
<code>Thayiye Nanna Devaru 1986</code>
<code>Na Ninna Preetisuve 1986</code>
<code>Agni Parikshe 1986</code>
<code>Rasthe Raja 1986</code>
<code>Samsarada Guttu 1986</code>
<code>Thayi 1987</code>
<code>Ee Bandha Anubandha 1987</code>
<code>Huli Hebbuli 1987</code>
<code>Digvijaya 1987</code>
<code>Lorry Driver 1987</code>
<code>Anthima Ghatta 1987</code>
<code>Mithileya Seetheyaru 1988</code>
<code>Dharmathma 1988</code>
<code>Sangliyana 1988</code>
<code>Shakthi 1988</code>
<code>Tarka 1989</code>
<code>Mahayuddha 1989</code>
<code>Anthintha Gandu Nanalla 1989</code>
<code>C B I Shankar 1989</code>
<code>Raja Simha 1989</code>
<code>Jayabheri 1989</code>
<code>Narasimha 1989</code>
<code>Wall Poster 1989</code>
<code>sp saangliyaana part 2 1990</code>
<code>Ramarajyadalli Rakshasaru 1990</code>
<code>Maheshwara 1990</code>
<code>Trinetra 1990</code>
<code>Aavesha 1990</code>
<code>Hosa Jeevana 1990</code>
<code>Halliya Surasuraru 1990</code>
<code>Bhale Chathura 1990</code>
<code>Aata Bombata 1990</code>
<code>Nigooda Rahasya 1990</code>
<code>Nagini 1991</code>
<code>Sundara Kanda 1991</code>
<code>Punda Prachanda 1991</code>
<code>Prana Snehitha 1992</code>"""

    AMBARISH = """<b>ರೆಬೆಲ್ ಸ್ಟಾರ್ ಅಂಬರೀಷ್</b>
<code>Naagarahaavu 1972</code>
<code>Bangarada Kalla 1973</code>
<code>Seethe alla savithri 1973</code>
<code>Chamundeshwari Mahime 1974</code>
<code>Mahadeshwara Pooja Phala 1975</code>
<code>Shubhamangala 1975</code>
<code>Bhagya Jyothi 1975</code>
<code>Nagakanye 1975</code>
<code>Onde Roopa Eradu guna 1975</code>
<code>Devara Kannu 1975</code>
<code>Hudugatada Hudugi 1976</code>
<code>Hosilu Mettida Hennu 1976</code>
<code>Bangarada Gudi 1976</code>"""
    
    AMBARISH1 = """<code>Snehada Sankole 1982</code>
<code>Ajith 1982</code>
<code>Tony 1982</code>
<code>Khadeema Kallaru 1992</code>
<code>Thirugu Baana 1983</code>
<code>Aasha 1983</code>
<code>Jaggu 1983</code>
<code>Avala Neralu 1983</code>
<code>Chakravyuha 1983</code>
<code>Matthe Vasantha 1983</code>
<code>Maneli Ramanna Beedili Kamanna 1983</code>
<code>Geluvu Nannade 1983</code>
<code>Hasida Hebbuli 1983</code>
<code>Dharma Yuddha 1983</code>
<code>Gajendra 1984</code>
<code>Gandu Bherunda 1984</code>
<code>Sidilu 1984</code>
<code>Guru Bhakti 1984</code>
<code>Onti Dhwani 1984</code>
<code>Rowdy Raja 1984</code>
<code>Mooru Janma 1984</code>
<code>Shapatha 1984</code>
<code>Onde Raktha 1984</code>
<code>Goonda Guru 1985</code>
<code>Guru Jagadguru 1985</code>
<code>Amara Jyothi 1985</code>
<code>Shabash Vikram 1985</code>
<code>Devara Mane 1985</code>
<code>Giri Baale 1985</code>
<code>Chaduranga 1985</code>
<code>Devarelliddane 1985</code>
<code>Masanada Hoovu 1985</code>
<code>Mamatheya Madilu 1985</code>
<code>Madhura Bandhavya 1986</code>
<code>Sathkara 1986</code>
<code>Mrugaalaya 1986</code>
<code>Brahmastra 1986</code>
<code>Preethi 1986</code>
<code>Matthondu Charitre 1986</code>
<code>Bete 1986</code>
<code>Vishwaroopa 1986</code>
<code>Bazar Bheema 1987</code>
<code>Olavina Udugore 9871</code>
<code>Prema Kadambari 1987</code>
<code>Mr Raja 1987</code>
<code>Poornachandra 1987</code>
<code>Antima Theerpu 1987</code>
<code>Digvijaya 1987</code>
<code>Inspector Krantikumar 1987</code>
<code>Bedi 1987</code>"""

    AMBARISH2 = """<code>Bandha Muktha 1987</code>
<code>Aapadbhandava 1987</code>
<code>Elu Suttina Kote 1987</code>
<code>Brahma Vishnu Maheshwara 1988</code>
<code>Praja Prabhutva 1988</code>
<code>Arjun 1988</code>
<code>Vijaya Khadga 1988</code>
<code>Nava Bharatha 1988</code>
<code>Ramanna Shamanna 1988</code>
<code>New Delhi 1988</code>
<code>Sangliyana 1988</code>
<code>Thayigobba Karna 1988</code>
<code>Hongkongnalli Agent Amar 1989</code>
<code>Jackey 1989</code>
<code>Guru 1989</code>
<code>Indrajith 1989</code>
<code>Gandandre Gandu 1989</code>
<code>Avatara Purusha 1989</code>
<code>Nyayakkagi Naanu 1989</code>
<code>Samsara Nouke 1989</code>
<code>Anthintha Gandu Nanalla 1989</code>
<code>Raja Yuvaraja 1989</code>
<code>Onti Salaga 1989</code>
<code>Jai Karnataka 1989</code>
<code>Jayabheri 1989</code>
<code>Matsara 1990</code>
<code>Nammoora Hammera 1990</code>
<code>Ranabheri 1990</code>
<code>Kempu Surya 1990</code>
<code>Kempu Gulabi 1990</code>
<code>Chakravarthy 1990</code>
<code>Ekalavya 1990</code>
<code>Rani Maharani 1990</code>
<code>Utkarsha 1990</code>
<code>Hrudaya Haadithu 1991</code>
<code>Kadana 1991</code>
<code>Kalachakra 1991</code>
<code>Puksatte Ganda hotte thumba unda 1991</code>
<code>Gandu Sidigundu 1991</code>
<code>Rowdy MLA 1991</code>
<code>Aranyadalli Abhimanyu 1991</code>
<code>Entede Bhanta 1992</code>
<code>Mysore Jaana 1992</code>
<code>Solillada Saradara 1992</code>
<code>Saptapadhi 1992</code>
<code>Bhanda Nanna Ganda 1992</code>
<code>Prema Sangama 1992</code>
<code>Megha Mandara 1992</code>
<code>Mallige Hoove 1992</code>
<code>Mannina Doni 1992</code>"""

    AMBARISH3 = """<code>Suryodaya 1993</code>
<code>Olavina Kanike 1993</code>
<code>Vasantha Poornima 1993</code>
<code>Midida Hrudayagalu 1993</code>
<code>Hrudaya Bandhana 1993</code>
<code>Munjaneya Manju 1993</code>
<code>Musuku 1994</code>
<code>Odahuttidavaru 1994</code> 
<code>Mandyada Gandu 1994</code>
<code>Vijaya Kankana 1994</code>
<code>Professor 1995</code>
<code>Kalyanotsava 1995</code>
<code>Betegara 1995</code>
<code>Balondu Chaduranga 1995</code>
<code>Karulina kudi 1995</code> 
<code>Operation Antha 1995</code>
<code>Mr Abhishek 1995</code>
<code>Palegara 1996</code>
<code>Mounaraga 1996</code>
<code>Rangena Halliyage Rangada Rangegowda 1997</code>
<code>Baalida Mane 1997</code>
<code>April Fool1997</code>
<code>Prema Geethe 1997</code>
<code>Habba 1999</code> 
<code>Devara maga 2000</code>  
<code>Vande Matharam 2000</code>
<code>Diggajaru 2001</code> 
<code>Prema Rajya</code>
<code>Annavru 2003</code> 
<code>Gowdru 2004</code> 
<code>Karnana Sampathu 2005</code>
<code>Pandavaru 2006</code> 
<code>Thandege thakka maga 2006</code> 
<code>Veera parampare 2010</code> 
<code>Vayuputra 2009</code> 
<code>Katari veera surasundarangi 2012</code> 
<code>Rana 2012</code>
<code>Bulbul 2013</code>
<code>Ambareesha 2014</code>
<code>Doddamane hudga 2016</code>
<code>Ambi ning vayassaytho 2018</code>
<code>Kurukshetra 2019</code>"""

    STATUS_TXT = """<b>★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code></b>"""

    LOG_TEXT_G = """#NewGroup
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,
ʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ..."""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}
ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?"""

    I_CUDNT = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 😕

ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ɪɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ 😃

ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

ᴇxᴀᴍᴘʟᴇ : Uncharted or Uncharted 2022 or Uncharted En

ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

ᴇxᴀᴍᴘʟᴇ : Loki S01 or Loki S01E04 or Lucifer S03E24

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)</b>"""

    I_CUD_NT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴏʀ ɪᴍᴅʙ..."""

    MVE_NT_FND = """ᴍᴏᴠɪᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ..."""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ Fᴏʀ Mᴏᴠɪᴇ Iɴ Dᴀᴛᴀʙᴀsᴇ..."""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""

    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : ᴊᴏᴇʟ ᴋᴜʀɪᴀɴ ʙɪᴊᴜ
• ᴜꜱᴇʀɴᴀᴍᴇ : @creatorbeatz
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href='t.me/creatorbeatz'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>"""

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ᴀꜰᴛᴇʀ 10 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ"""

    MINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Uncharted

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ : </b> <code>{file_name}</code>"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10</b>"""
    
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """
<b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
    
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    LOGO = """

██████╗░░██████╗░░░░░░░████████╗██╗░░██╗███████╗░░░░░░███████╗██╗██╗░░░░░███████╗░░░░░░██████╗░░█████╗░███╗░░██╗░█████╗░██████╗░
██╔══██╗██╔═══██╗░░░░░░╚══██╔══╝██║░░██║██╔════╝░░░░░░██╔════╝██║██║░░░░░██╔════╝░░░░░░██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗
██║░░██║██║██╗██║█████╗░░░██║░░░███████║█████╗░░█████╗█████╗░░██║██║░░░░░█████╗░░█████╗██║░░██║██║░░██║██╔██╗██║██║░░██║██████╔╝
██║░░██║╚██████╔╝╚════╝░░░██║░░░██╔══██║██╔══╝░░╚════╝██╔══╝░░██║██║░░░░░██╔══╝░░╚════╝██║░░██║██║░░██║██║╚████║██║░░██║██╔══██╗
██████╔╝░╚═██╔═╝░░░░░░░░░░██║░░░██║░░██║███████╗░░░░░░██║░░░░░██║███████╗███████╗░░░░░░██████╔╝╚█████╔╝██║░╚███║╚█████╔╝██║░░██║
╚═════╝░░░░╚═╝░░░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░░░░░░╚═╝░░░░░╚═╝╚══════╝╚══════╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝"""
