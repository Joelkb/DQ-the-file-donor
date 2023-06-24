class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ {},
Mʏ Nᴀᴍᴇ Is <a href=https://t.me/{}>{}</a>, I Cᴀɴ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs, Jᴜsᴛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Eɴᴊᴏʏ 😍</b>"""

    RECENT = """<b>Recently Uploaded New Movies</b>
<code>Karthavya 2023</code>
<code>Malikappuram</code>
<code>Huli</code> (tamil puli)
<code>Narasimha</code> (shankar nag old movie)
<code>Gadiraja</code>
<code>Parugu</code>
<code>Alluri 2023</code>
<code>I Love You 2023</code>
<code>Stand Up Rahul 2023</code>
<code>Shri Balaji Photo Studio 2023</code>
<code>Bhikshuka 2 2023</code>"""

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
<code>Bangarada Gudi 1976</code>
<code>Kanasu Nanasu 1976</code>
<code>Kudure Mukha 1977</code>
<code>Nagarahole 1977</code>
<code>Maagiya Kanasu 1977</code>
<code>Manasinanthe Mangalya 1977</code>
<code>Mugdha Manava 1977</code>
<code>Chinna Ninna Muddaduve 1977</code>
<code>Banashankari 1977</code>
<code>Halli Haida 1978</code>
<code>Havina Hejje 1978</code>
<code>Muyyige Muyyi 1978</code>
<code>Siritanakke Savaal 1978</code>
<code>Paduvaaralli Pandavaru 1978</code>
<code>Sneha Sedu 1978</code>
<code>Amarnath 1978</code>
<code>Kiladi Jodi 1978</code>
<code>Balu Aparoopa Nam Jodi 1978</code>
<code>Pakka Kalla 1979</code>
<code>Kamala 1979</code>
<code>Putani Agent 123 1979</code>
<code>Savathiya Neralu 1979</code>
<code>Dhairya Lakshmi 1980</code>
<code>Vajrada Jalapatha 1980</code>
<code>Ondu Hennu Aaru Kannu 1980</code>
<code>Subbi Subbakka Suvvalali 1980</code>
<code>Nyaya Neethi Dharma 1980</code>
<code>Leader Vishwanath 1981</code>
<code>Ranganayaki 1981</code>
<code>Antha 1981</code>
<code>Maha Prachandaru 1981</code>
<code>Snehitara Savaal 1981</code>
<code>Bhaari Bharjari Bete 1981</code>
<code>Avala Hejje 1981</code>"""
    
    AMBARISH1 = """<code>Shankar Sundar1982</code>
<code>Prema Matsara 1982</code>
<code>Maava Sose Savaal 1982</code>
<code>Snehada Sankole 1982</code>
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
<code>Antima Theerpu 1987</code>"""

    AMBARISH2 = """<code>Digvijaya 1987</code>
<code>Inspector Krantikumar 1987</code>
<code>Bedi 1987</code>
<code>Bandha Muktha 1987</code>
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
<code>Prema Sangama 1992</code>"""

    AMBARISH3 = """<code>Megha Mandara 1992</code>
<code>Mallige Hoove 1992</code>
<code>Mannina Doni 1992</code>
<code>Suryodaya 1993</code>
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

    VISHNUVARDHAN = """<b>ಸಾಹಸ ಸಿಂಹ ವಿಷ್ಣುವರ್ಧನ್</b>
<code>naagarahaavu 1972</code>
<code>mane belagidha sose 1973</code>
<code>gandhada gudi 1973</code>
<code>seethe alla savithri 1973</code>
<code>anna attige 1974</code>
<code>bhootayyana maga ayyu 1974</code>
<code>koodi balona 1975</code>
<code>devara gudi 1975</code>
<code>onde roopa eradu guna 1975</code>
<code>kalla kulla 1975</code>
<code>Nagakanye 1975</code>
<code>bangarada gudi 1976</code>
<code>Devaru Kotta Vara 1976</code>
<code>makkala bhagya 1976</code>
<code>Devaru Kotta Vara 1977</code>
<code>Bayasade Banda Bhagya 1977</code>
<code>Chinna Ninna Muddaduve 1977</code>
<code>sahodarara savaal 1977</code>
<code>Sose Tanda Soubhagya 1977</code>
<code>Nagarahole 1977</code>
<code>vamsha jyothi 1978</code>
<code>kiladi kittu 1978</code>
<code>Siritanakke Savaal 1978</code>
<code>sneha sedu 1978</code>
<code>Nanna Prayaschittha 1978</code>
<code>muyyige muyyi 1978</code>
<code>bhale huduga 1978</code>
<code>kiladi jodi 1978</code>
<code>Singaporenalli Raja Kulla 1978</code>
<code>asadhya aliya 1979</code>
<code>vijay vikram 1979</code>
<code>naniruvude ninagagi 1979</code>
<code>nentaro gantu kallaro 1979</code>
<code>nanna rosha nooru varusha 1980</code>
<code>rama parushurama 1980</code>
<code>hanthakana sanchu 1980</code>
<code>rahasya rathri 1980</code>
<code>simha jodi 1980</code>
<code>biligiriy banadalli 1980</code>
<code>bangarada jinke 1980</code>
<code>avala hejje 1981</code>
<code>maha prachandaru 1981</code>
<code>naga kala bhairava 1981</code>
<code>mane mane kathe 1981</code>
<code>Snehitara Savaal 1981</code>"""

    VISHNUVARDHAN1 = """<code>Preetisi Nodu 1981</code>
<code>Sahasasimha 1982</code>
<code>karmika kallanalla 1982</code>
<code>jimmy gallu 1982</code>
<code>suvarna sethuve 1982</code>
<code>oorige upakari 1982</code>
<code>kallu veene nudiyithu 1982</code>
<code>gandugali rama 1983</code>
<code>sididedda sahodara 1983</code>
<code>gandharva giri 1983</code>
<code>chinnadantha maga 1983</code>
<code>Simha Garjane 1983</code>
<code>benki birugali 1984</code>
<code>indina ramayana 1984</code>
<code>rudranaga 1984</code>
<code>Khaidi 1984</code>
<code>Bandhana 1984</code>
<code>nee thanda kanike 1985</code>
<code>karthavya 1985</code>
<code>jeevana chakra 1985</code>
<code>maha purusha 1985</code>
<code>nee bareda kadambari 1985</code>
<code>veeradhi veera 1985</code>
<code>nanna prathigne 1985</code>
<code>mareyada manikya 1985</code>
<code>kathanayaka 1986</code>
<code>ee jeeva ninagagi 1986</code>
<code>krishna nee begane baro 1986</code>
<code>malaya marutha 1986</code>
<code>sathya jyothi 1986</code>
<code>karna 1986</code>
<code>sathyam shivam sundaram 1987</code>
<code>shubha milana 1987</code>
<code>jeevana jyothi 1987</code>
<code>karunamayi 1987</code>
<code>Aaseya Bale 1987</code>
<code>sowbhagya lakshmi 1987</code>
<code>jayasimha 1987</code>
<code>December 31 1988</code>
<code>olavina aasare 1988</code>
<code>nammoora raja 1988</code>
<code>jana nayaka 1988</code>
<code>Suprabhatha 1988</code>
<code>krishna rukmini 1988</code>
<code>daada 1988</code>"""

    VISHNUVARDHAN2 = """<code>deva 1989</code>
<code>doctor krishna 1989</code>
<code>ondagi balu 1989</code>
<code>hrudaya geethe 1989</code>
<code>rudra 1989</code>
<code>mathe haditu kogile 1990</code>
<code>shivashankar 1990</code>
<code>muthina haara 1990</code>
<code>Neenu Nakkare Haalu Sakkare 1991</code>
<code>jagadeka veera 1991</code>
<code>lion jagapathi rao 1991</code>
<code>ravivarma 1992</code>
<code>harakeya kuri 1992</code>
<code>rajadhi raja 1992</code>
<code>Nanna Shathru 1992</code>
<code>Rayaru Bandaru Mavana Manege 1993</code>
<code>manikantana mahime 1993</code>
<code>sangharsha 1993</code>
<code>Nanendu Nimmavane 1993</code>
<code>Vishnu Vijaya 1993</code>
<code>kiladigalu 1994</code>
<code>nishkarsha 1994</code>
<code>samrat 1994</code>
<code>kunthi puthra 1994</code>
<code>time bomb 1994</code>
<code>himapatha 1995</code>
<code>karulina kudi 1995</code>
<code>bangarada kalasa 1995</code>
<code>yama kinkara 1995</code>
<code>halunda thavaru 1995</code>
<code>karnataka suputra 1996</code>
<code>hello daddy 1996</code>
<code>jeevanadhi 1996</code>
<code>dhani 1996</code>
<code>mojugara sogasugara 1996</code>
<code>appaji 1996</code>
<code>Baalina Jyothi 1996</code>
<code>mangalasoothra 1997</code>
<code>ellaranthalla nanna ganda 1997</code>
<code>janani janmabhoomi 1997</code>
<code>Laali 1997</code>
<code>nishyabda 1998</code>
<code>surya vamsha 1999</code>
<code>Habba 1999</code>
<code>veerappa nayaka 1999</code>"""

    VISHNUVARDHAN3 = """<code>deepavali 2000</code>
<code>Yajamana 2000</code> 
<code>Soorappa 2000</code> 
<code>Diggajaru 2001</code> 
<code>Kotigobba 2001</code> 
<code>Parva 2002</code> 
<code>Jamindaru 2002</code>
<code>Simhadriya simha 2002</code> 
<code>Raja narasimha 2003</code> 
<code>Hrudayavantha 2003</code> 
<code>Jyeshtha 2004</code>
<code>Sahukara 2004</code> 
<code>apthamitra 2004</code>
<code>kadamba 2004</code> 
<code>Vishnu sena 2005</code> 
<code>Varsha 2005</code>
<code>Sirivantha 2006</code>
<code>Neenello naanalle 2006</code> 
<code>ekadantha 2007</code> 
<code>maathaad maathaadu mallige 2007</code>
<code>Ee Bandhana 2007</code>
<code>Nam Yajamanru 2008</code>
<code>Bellary Naga 2009</code>
<code>School master 2010</code> 
<code>Aptharakshaka 2010</code>"""

    RAJKUMAR = """<b>ನಟಸಾರ್ವಭೌಮ ಡಾ. ರಾಜ್‌ಕುಮಾರ್</b>
<code>bedara kannappa 1954</code>
<code>sodari 1955</code>
<code>bhakta vijaya 1956</code>
<code>ohileshwara 1956</code>
<code>hari bhakta 1956</code>
<code>rayara sose 1957</code>
<code>anna thangi 1958</code>
<code>bhookailasa 1958</code>
<code>shree krishna gaarudi 1958</code>
<code>jagajyothi basveshwara 1959</code>
<code>dharma vijaya 1959</code>
<code>mahishasura mardini 1959</code>
<code>dashavathara 1960</code>
<code>ranadheera kanteerava 1960</code>
<code>rani honnamma 1960</code>
<code>aasha sundari 1960</code>
<code>bhakta kanakadasa 1960</code>
<code>kittur chennamma 1961</code>
<code>kantheredu nodu 1961</code>
<code>kaiwara mahathme 1961</code>
<code>bhakta cheta 1961</code>
<code>nagarjuna 1961</code>
<code>sri shaila mahathme 1961</code>
<code>gaali gopura 1962</code>
<code>karuneye kutumbada kannu 1962</code>
<code>swarna gowri 1962</code>
<code>bhoodaana 1962</code>
<code>mahathma kabir 1962</code>
<code>devasundari 1962</code>
<code>thejaswini 1962</code>
<code>nanda deepa 1963</code>
<code>valmiki 1963</code>
<code>gowri 1963</code>
<code>kanyarathna 1963</code>
<code>kulavadhu 1963</code>
<code>jeevana tharanga 1963</code>
<code>saaku magalu 1963</code>
<code>veerakesari 1963</code>
<code>sathi shakthi 1963</code>
<code>mana mecchida madadi 1963</code>
<code>sri ramanjaneya yuddha 1963</code>
<code>chandra kumara 1963</code>
<code>santha thukaram 1963</code>
<code>navakoti narayana 1964</code>
<code>chandavalliya thota 1964</code>
<code>shivagange mahathme 1964</code>
<code>tumbida koda 1964</code>
<code>prathigne 1964</code>"""

    RAJKUMAR1 = """<code>muriyada mane 1964</code>
<code>naandi 1964</code>
<code>annapoorna 1964</code>
<code>chandrahasa 1965</code>
<code>sarvagna murthy 1965</code>
<code>vaatsalya 1965</code>
<code>mahasathi anasuya 1965</code>
<code>ide mahasudina 1965</code>
<code>satya harishchandra 1965</code>
<code>bettada huli 1965</code>
<code>sati savithri 1965</code>
<code>maduve madi nodu 1965</code>
<code>premamayi 1966</code>
<code>bala nagamma 1966</code>
<code>mantralaya mahatme 1966</code>
<code>katari veera 1966</code>
<code>kilaadi ranga 1966</code>
<code>madhumalathi 1966</code>
<code>emme thammanna 1966</code>
<code>gange gowri 1967</code>
<code>sathi sukanya 1967</code>
<code>parvathi kalyana 1967</code>
<code>rajashekara 1967</code>
<code>lagna pathrike 1967</code>
<code>devara gedda manava 1967</code>
<code>manassiddare maarga 1967</code>
<code>bangarada hoovu 1967</code>
<code>beedi basavanna 1967</code>
<code>chakra theertha 1967</code>
<code>immadi pulakeshi 1967</code>
<code>gandhinagara 1978</code>
<code>manassakshi 1968</code>
<code>sarvamangala 1968</code>
<code>bhagya devathe 1968</code>
<code>bhagyada bagilu 1968</code>
<code>hannele chiguridaga 1968</code>
<code>bangalore mail 1968</code>
<code>hannele chiguridaga 1968</code>
<code>bhagyada bagilu 1968</code>
<code>rowdi ranganna 1968</code>
<code>dhoomaketu 1968</code>
<code>amma 1968</code>
<code>simhaswapna 1968</code>
<code>goa dalli cid 999 1968</code>
<code>mannina maga 1968</code>
<code>margadarshi 1969</code>
<code>gandondu hennaru 1969</code>
<code>mallammana pavada 1969</code>
<code>choori chikkanna 1969</code>
<code>punarjanma 1969</code>"""

    RAJKUMAR2 = """<code>bhale raja 1969</code>
<code>uyyale 1969</code>
<code>chikkamma 1969</code>
<code>mayor muthanna 1969</code>
<code>sri krishnadevaraya 1970</code>
<code>hasiru thorana 1970</code>
<code>karulina kare 1970</code>
<code>cid rajanna 1970</code>
<code>paropakari 1970</code>
<code>mr rajkumar 1970</code>
<code>devara makkalu 1970</code>
<code>nadina bhagya 1970</code>
<code>Baalu Belagithu 1970</code>
<code>kasturi nivasa 1971</code>
<code>kula gourava 1971</code>
<code>thayi devaru 1971</code>
<code>kasidre kailasa 1971</code>
<code>Nyayave Devaru 1971</code>
<code>baala bandhana 1971</code>
<code>sakshatkara 1971</code>
<code>nyayave devaru 1971</code>
<code>pratidwani 1971</code>
<code>sri krishna rukmini satyabhama 1971</code>
<code>janma rahasya 1972</code>
<code>sipayi ramu 1972</code>
<code>hrudaya sangama 1972</code>
<code>bangaarada manushya 1972</code>
<code>kranti veera 1972</code>
<code>jaga mecchida maga 1972</code>
<code>Nanda Gokula 1972</code>
<code>Bhale Huchcha 1972</code>
<code>swayamvara 1973</code>
<code>devaru kotta thangi 1973</code>
<code>doorada betta 1973</code>
<code>Gandhada Gudi 1973</code>
<code>mooroovare vajragalu 1973</code>
<code>Eradu Kanasu 1974</code>
<code>bangaarada panjara 1974</code>
<code>sri srinivasa kalyana 1974</code>
<code>sampathige saval 1974</code>
<code>Bhakta Kumbara 1974</code>
<code>mayura 1975</code>
<code>daari tappida maga 1975</code>
<code>Trimurti 1975</code>
<code>naa ninna mareyalare 1976</code>
<code>premada kanike 1976</code>
<code>bahaddur gandu 1976</code>
<code>raja nanna raja 1976</code>
<code>badavara bandhu 1976</code>
<code>Babruvahana 1977</code>"""

    RAJKUMAR3 = """<code>bhagyavantharu 1977</code>
<code>giri kanye 1977</code>
<code>sanaadi appanna 1977</code>
<code>olavu geluvu 1977</code>
<code>operation diamond racket 1978</code>
<code>thayige thakka maga 1978</code>
<code>shankar guru 1978</code>
<code>nanobba kalla 1979</code>
<code>huliya haalina mevu 1979</code>
<code>ravichandra 1980</code>
<code>Vasanta Geetha 1980</code>
<code>keralida simha 1981</code>
<code>Nee Nanna Gellalare 1981</code>
<code>Haavina Hede 1981</code>
<code>Chalisuva Modagalu 1982</code>
<code>hosa belaku 1982</code>
<code>haalu jenu 1982</code>
<code>Kaamana Billu 1983</code>
<code>kaviratna kalidasa 1983</code>
<code>Eradu Nakshatragalu 1983</code>
<code>Bhakta Prahlada 1983</code>
<code>samayada gombe 1984</code>
<code>shravana banthu 1984</code>
<code>yarivanu 1984</code>
<code>ade kannu 1985</code>
<code>dhruva thare 1985</code>
<code>jwaalamukhi 1985</code>
<code>Guri 1986</code>
<code>Anuraga Aralithu 1986</code>
<code>bhagyada lakshmi baramma 1986</code>
<code>shruthi seridaaga 1987</code>
<code>ondu muttina kathe 1987</code>
<code>devatha manushya 1988</code>
<code>jeevana chaitra 1989</code>
<code>jeevana chaitra 1992</code>
<code>aakasmika 1993</code>
<code>Odahuttidavaru 1994</code>
<code>Shabdavedhi 2000</code>"""

    SHIVARAJKUMAR = """<b>ಕರುನಾಡ ಚಕ್ರವರ್ತಿ ಹ್ಯಾಟ್ರಿಕ್ ಹೀರೋ ಡಾ. ಶಿವ ರಾಜ್ ಕುಮಾರ್</b>
<code>sri srinivasa kalyana 1974</code> (ಬಾಲ ನಟ)
<code>Anand 1986</code>
<code>ratha sapthami 1986</code>
<code>mana mecchida hudugi 1987</code>
<code>Shiva Mecchida Kannappa 1988</code>
<code>Samyuktha 1988</code>
<code>Ranaranga 1988</code>
<code>Inspector Vikram 1989</code>
<code>ade raaga ade haadu 1989</code>
<code>mruthyunjaya 1990</code>
<code>Aasegobba Meesegobba 1990</code>
<code>Modada mareyalli 1991</code>
<code>aralida hoovugalu 1991</code>
<code>midida shruthi 1992</code>
<code>Purushotthama 1992</code>
<code>Mavanige Thakka aliya 1992</code>
<code>Jaga mechhida huduga 1993</code>
<code>chirabandhavya 1993</code>
<code>Gandhada Gudi Part 2 1994</code>
<code>gandugali 1994</code>
<code>mutthanna 1994</code>
<code>Om 1995</code>
<code>Gadibidi Aliya 1995</code>
<code>savyasachi 1995</code>
<code>samara 1995</code>
<code>dore 1995</code>
<code>mana midiyithu 1995</code>
<code>Shiva sainya 1996</code>
<code>Gajanura Gandu 1996</code>
<code>janumada jodi 1996</code>
<code>annavara makkalu 1996</code>
<code>Aadhitya 1996</code>
<code>Ibbara Naduve Muddina Aata 1996</code>
<code>ganga yamuna 1997</code>
<code>Simhada Mari 1997</code>
<code>Ammavra Ganda 1997</code>
<code>muddina kanmani 1997</code>
<code>Jodi Hakki 1997</code>
<code>prema raga haadu gelathi 1997</code>
<code>raaja 1997</code>
<code>nammoora huduga 1998</code>
<code>andaman 1998</code>
<code>mr putsami 1998</code>
<code>bhoomi thayiya chochchala maga 1998</code>
<code>gadibidi krishna 1998</code>
<code>Kurubana rani 1998</code>
<code>chandrodaya 1999</code>
<code>Hrudaya hrudaya 1999</code>"""

    SHIVARAJKUMAR1 = """<code>A K 47 1999</code>
<code>Janumadatha 1999</code>
<code>Vishwa 1999</code>
<code>Yare Nee Abhimani 2000</code>
<code>Preethse 2000</code>
<code>Hagalu vesha 2000</code>
<code>Indradhanush 2000</code>
<code>Krishna Leele 2000</code>
<code>Devara maga 2000</code>
<code>Galate aliyandru 2000</code>
<code>Maduve aagona baa 2001</code>
<code>Asura 2001</code>
<code>Bahala chennagide 2001</code>
<code>Baava Baamaida 2001</code>
<code>Sundara kanda 2001</code>
<code>Yuvaraja 2001</code>
<code>Jodi 2001</code>
<code>Kodanda rama 2002</code>
<code>Ninne Preethisuve 2002</code>
<code>Thavarige Baa Thangi 2002</code>
<code>Sriram 2003</code>
<code>Nanjundi 2003</code>
<code>Chigurida kanasu 2003</code>
<code>smile 2003</code>
<code>Rowdy aliya 2004</code>
<code>Sarvabhouma 2004</code>
<code>Kanchana ganga 2004</code>
<code>Rishi 2005</code>
<code>Rakshasa 2005</code>
<code>Valmiki 2005</code>
<code>Jogi 2005</code>
<code>Anna thangi 2005</code>
<code>Ashoka 2006</code>
<code>Thavarina siri 2006</code>
<code>Gandugali kumara rama 2006</code>
<code>Thayiya Madilu 2007</code>
<code>Santha 2007</code>
<code>Gandana mane 2007</code>
<code>Lava Kusha 2007 </code>
<code>Sathya In Love</code>
<code>Bandhu balaga 2008 </code>
<code>Madesha 2008</code>
<code>Paramesha Paanwala 2008</code>
<code>Nanda 2009</code>
<code>Hatrick Hodi Maga 2009</code>
<code>Devaru kotta thangi 2009</code>
<code>Bhagyada Balegara 2009</code>
<code>Sugreeva 2010</code>
<code>Thamassu 2010</code>
<code>Cheluveye ninne nodalu 2010</code>"""

    SHIVARAJKUMAR2 = """<code>Mylari 2010</code>
<code>Jogayya 2011</code>
<code>shiva 2012</code>
<code> Kaddipudi 2013</code>
<code>Lakshmi 2013</code>
<code>Andhar Bahar 2013</code>
<code>Kaddipudi 2013</code>
<code>Bhajarangi 2013</code>
<code>Aaryan 2014 </code>
<code>Vajrakaya 2015</code>
<code>Belli 2014</code>
<code>Killing veerappan 2016</code>
<code>Shivalinga 2016</code>
<code>Santheyalli nintha kabira 2016</code>
<code>Srikanta 2017</code>
<code>Bangara so bangarada manushya 2017</code>
<code>Mass leader 2017</code>
<code>Mufti 2017</code>
<code>Tagaru 2018</code>
<code>The villain 2018</code>
<code>Kavacha 2019</code>
<code>Rustum 2019</code>
<code>Ayushman bhava 2019</code>
<code>Drona 2020</code>
<code>Bhajarangi2 2021</code>
<code>James 2022</code>
<code>bairagee 2022</code>
<code>vedha 2022</code>
<code>kabzaa 2022</code>"""

    SUDEEP = """<b>ಅಭಿನಯ ಚಕ್ರವರ್ತಿ ಕಿಚ್ಚ ಸುದೀಪ್</b>
<code>thayavva 1997</code>
<code>Sparsha 2000</code>
<code>Huchcha 2001</code>
<code>Vaalee 2001</code>
<code>Chandu 2002</code>
<code>Dhumm 2002</code>
<code>Nandhi 2002</code>
<code>Kiccha 2003</code>
<code>Partha 2003</code>
<code>Swathi muthu 2003</code>
<code>Ranga sslc 2004</code>
<code>Nalla 2004 </code>
<code>Maharaja 2005</code>
<code>Kashi from village 2005</code>
<code>Nammanna 2005</code>
<code>My autograph 2006</code>
<code>Thirupathi 2006</code>
<code>No73 shanthi nivasa 2007</code>
<code>Hubli 2006</code>
<code>Gooli 2008</code>
<code>Mussanjemaatu 2008</code>
<code>Kaamannana makkalu 2008</code>
<code>Mast Maja Maadi 2008</code>
<code>Veera madakari 2009</code>
<code>Just maath maathalli 2010</code>
<code>Mr Theertha 2010</code>
<code>Kiccha Huccha 2010</code>
<code>Veera parampare 2010</code>
<code>Kempe gowda 2011</code>
<code>Vishnuvardhana 2011</code>
<code>Varadhanayaka 2013</code>
<code>Bachchan 2013</code>
<code>Maanikya 2014</code>
<code>Ranna 2015</code>
<code>Kotigobba 2 2016</code>
<code>Mukunda murari 2016 </code>
<code>Hebbuli 2017</code>
<code>The villain 2018</code>
<code>Pailwan 2019</code>
<code>Kotigobba 3 2021</code>
<code>Vikrant Rona 2022</code>
<code>Kabzaa 2023</code>"""

    GANESH = """<b>ಗೋಲ್ಡನ್ ಸ್ಟಾರ್ ಗಣೇಶ್</b>
<code>mungaaru male 2006</code>
<code>chellata 2006</code>
<code>hudugaata 2007</code>
<code>cheluvina chittara 2007</code>
<code>krishna 2007</code>
<code>Gaalipata 2008</code>
<code>aramane 2008</code>
<code>bombaat 2008</code>
<code>sangama 2008</code>
<code>circus 2009</code>
<code>maleyali joteyali 2009</code>
<code>ullasa uthsaha 2010</code>
<code>yeno onthara 2010</code>
<code>kool 2011</code>
<code>maduve mane 2011</code>
<code>shyloo 2011</code>
<code>munjaane 2012</code>
<code>mr 420 2012</code>
<code>auto raaja 2012</code>
<code>sakkare 2012</code>
<code>Romeo 2012</code>
<code>shravani subramanya 2013</code>
<code>dil rangeela 2014</code>
<code>kushi kushiyaagi 2015</code>
<code>buguri 2015</code>
<code>style king 2016</code>
<code>zoom 2016</code>
<code>mungaaru male 2 2016</code>
<code>sundaranga jaana 2016</code>
<code>pataaki 2017</code>
<code>Mugulu nage 2017</code>
<code>chamak 2017</code>
<code>orange 2018</code>
<code>99 2019</code>
<code>gimmick 2019</code>
<code>geetha 2019</code>
<code>Sakath 2021</code>
<code>Gaalipata 2 2022</code>
<code>Triple Riding 2022</code>"""

    DARSHAN = """<b>ಚಾಲೆಂಜಿಂಗ್ ಸ್ಟಾರ್ ದರ್ಶನ್</b>
<code>Majestic 2002</code>
<code>dhruva 2002</code>
<code>Ninagoskara 2002</code>
<code>kitty 2002</code>
<code>kariya 2003</code>
<code>laali haadu 2003</code>
<code>lankesh patrike 2003</code>
<code>namma preethiya ramu 2003</code>
<code>dasa 2003</code>
<code>Annavru 2003</code>
<code>dharma 2004</code>
<code>darshan 2004</code>
<code>bhagawan 2004</code>
<code>kalasipalya 2004</code>
<code>ayya 2005</code>
<code>shastri 2005</code>
<code>swamy 2005</code>
<code>mandya 2006 </code>
<code>suntaragaali 2006</code>
<code>dattha 2006</code>
<code>thangigagi 2006</code>
<code>Bhoopathi 2007</code>
<code>snehana preethina 2007</code>
<code>anatharu 2007</code>
<code>gaja 2008</code>
<code>Indra 2008</code>
<code>Arjun 2008</code>
<code>navagraha 2008</code>
<code>yodha 2009</code>
<code>abhay 2009</code>
<code>Porki 2010</code>
<code>shourya 2010</code>
<code>boss 2011</code>
<code>saarathi 2011</code>
<code>chingari 2012</code>
<code>krantiveera sangolli rayanna 2012</code>
<code>bulbul 2013</code>
<code>Brundaavana 2013</code>
<code>ambareesha 2014</code>
<code>mr airavata 2015</code>
<code>Viraat 2016</code>
<code>jaggu dada 2016</code>
<code>chakravarthy 2017</code>
<code>Tarak 2017</code>
<code>Yajamana 2019</code>
<code>kurukshetra 2019</code>
<code>Odeya 2019</code>
<code>Robert 2021</code>"""

    DARSHAN1 = """<code>Kranti 2023</code>"""
    
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
