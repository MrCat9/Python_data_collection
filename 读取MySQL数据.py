cursor.execute()  #得到总记录数
cursor.fetchone()  #查询下一行
cursor.fetchmany(size=None)  #得到指定条数
cursor.fetchall()  #得到全部
connection.close()  #关闭连接



#
import pymysql

import io  
import sys  
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

connection = pymysql.connect(  #获取连接
            host='localhost',
            user='root',
            passwd='123456',
            db='pymysql_test01',
            charset='utf8mb4'
            )

try:
    with connection.cursor() as cursor:  #获取会话指针
        sql = 'select `urlname`,`urlhref` from `urls` where `id` is not null'  #查询语句
        count = cursor.execute(sql)
        print(count)  #168
#下面这样写也可以，但是*占用资源较多
#         sql = 'select * from urls where `id` is not null'
#         print(cursor.execute(sql))  #168
#         sql = 'select * from urls'
#         print(cursor.execute(sql))  #168     
        
        result = cursor.fetchmany(3)  #得到第1--3条
        print(result)  #(('Wikipedia', 'https://en.wikipedia.org/wiki/Wikipedia'), ('free', 'https://en.wikipedia.org/wiki/Free_content'), ('encyclopedia', 'https://en.wikipedia.org/wiki/Encyclopedia'))
        result = cursor.fetchmany(size = 3)  #得到第4--6条
        print(result)  #(('anyone can edit', 'https://en.wikipedia.org/wiki/Wikipedia:Introduction'), ('5,590,367', 'https://en.wikipedia.org/wiki/Special:Statistics'), ('English', 'https://en.wikipedia.org/wiki/English_language'))
        result = cursor.fetchall()  #得到第7--168条
        print(result)  #(('Arts', 'https://en.wikipedia.org/wiki/Portal:Arts'), ('Biography', 'https://en.wikipedia.org/wiki/Portal:Biography'), ('Geography', 'https://en.wikipedia.org/wiki/Portal:Geography'), ('History', 'https://en.wikipedia.org/wiki/Portal:History'), ('Mathematics', 'https://en.wikipedia.org/wiki/Portal:Mathematics'), ('Science', 'https://en.wikipedia.org/wiki/Portal:Science'), ('Society', 'https://en.wikipedia.org/wiki/Portal:Society'), ('Technology', 'https://en.wikipedia.org/wiki/Portal:Technology'), ('All portals', 'https://en.wikipedia.org/wiki/Portal:Contents/Portals'), ('', 'https://en.wikipedia.org/wiki/File:Marie_Aug_24_2014_1830Z.png'), ('Hurricane Marie', 'https://en.wikipedia.org/wiki/Hurricane_Marie_(2014)'), ('seventh-most intense', 'https://en.wikipedia.org/wiki/List_of_the_most_intense_tropical_cyclones#Eastern_Pacific_Ocean'), ('Pacific hurricane', 'https://en.wikipedia.org/wiki/Pacific_hurricane'), ('barometric pressure', 'https://en.wikipedia.org/wiki/Barometric_pressure'), ('mbar', 'https://en.wikipedia.org/wiki/Bar_(unit)'), ('hPa', 'https://en.wikipedia.org/wiki/Pascal_(unit)'), ('inHg', 'https://en.wikipedia.org/wiki/Inches_of_Mercury'), ('California', 'https://en.wikipedia.org/wiki/California'), ('Los Cabos', 'https://en.wikipedia.org/wiki/Los_Cabos'), ('Colima', 'https://en.wikipedia.org/wiki/Colima'), ('Oaxaca', 'https://en.wikipedia.org/wiki/Oaxaca'), ('outer bands', 'https://en.wikipedia.org/wiki/Rainband'), ('swells', 'https://en.wikipedia.org/wiki/Swell_(ocean)'), ('Santa Catalina Island', 'https://en.wikipedia.org/wiki/Santa_Catalina_Island,_California'), ('Greater Los Angeles Area', 'https://en.wikipedia.org/wiki/Greater_Los_Angeles_Area'), ('breakwater', 'https://en.wikipedia.org/wiki/Breakwater_(structure)'), ('Long Beach', 'https://en.wikipedia.org/wiki/Long_Beach,_California'), ('Malibu', 'https://en.wikipedia.org/wiki/Malibu,_California'), ('Full\xa0article...', 'https://en.wikipedia.org/wiki/Hurricane_Marie_(2014)'), ('Ferugliotherium', 'https://en.wikipedia.org/wiki/Ferugliotherium'), ('Thomas Riley Marshall', 'https://en.wikipedia.org/wiki/Thomas_Riley_Marshall'), ('Winter War', 'https://en.wikipedia.org/wiki/Winter_War'), ('Archive', 'https://en.wikipedia.org/wiki/Wikipedia:Today%27s_featured_article/March_2018'), ('More featured articles', 'https://en.wikipedia.org/wiki/Wikipedia:Featured_articles'), ('Zofia Posmysz', 'https://en.wikipedia.org/wiki/Zofia_Posmysz'), ('Auschwitz', 'https://en.wikipedia.org/wiki/Auschwitz_concentration_camp'), ('Passenger', 'https://en.wikipedia.org/wiki/Passenger_(Posmysz_novel)'), ('a 1963 film', 'https://en.wikipedia.org/wiki/Passenger_(1963_film)'), ('a 1968 opera', 'https://en.wikipedia.org/wiki/The_Passenger_(opera)'), ('Seycellesa', 'https://en.wikipedia.org/wiki/Seycellesa'), ('nematode', 'https://en.wikipedia.org/wiki/Nematode'), ('Traklosia', 'https://en.wikipedia.org/wiki/Traklosia'), ('William Strudwick Arrasmith', 'https://en.wikipedia.org/wiki/William_Strudwick_Arrasmith'), ('Greyhound', 'https://en.wikipedia.org/wiki/Greyhound_Lines'), ('Australian Air Corps', 'https://en.wikipedia.org/wiki/Australian_Air_Corps'), ('Luo Haocai', 'https://en.wikipedia.org/wiki/Luo_Haocai'), ("Supreme People's Court", 'https://en.wikipedia.org/wiki/Supreme_People%27s_Court'), ('Tillie Walden', 'https://en.wikipedia.org/wiki/Tillie_Walden'), ('graphic novel', 'https://en.wikipedia.org/wiki/Graphic_novel'), ('Spinning', 'https://en.wikipedia.org/wiki/Spinning_(comics)'), ('figure skater', 'https://en.wikipedia.org/wiki/Figure_skater'), ('Center for Cartoon Studies', 'https://en.wikipedia.org/wiki/Center_for_Cartoon_Studies'), ('Amy Coney Barrett', 'https://en.wikipedia.org/wiki/Amy_Coney_Barrett'), ('Blackstone Legal Fellowship', 'https://en.wikipedia.org/wiki/Blackstone_Legal_Fellowship'), ('solar eclipse of May 20, 2012', 'https://en.wikipedia.org/wiki/Solar_eclipse_of_May_20,_2012'), ('Archive', 'https://en.wikipedia.org/wiki/Wikipedia:Recent_additions'), ('Start a new article', 'https://en.wikipedia.org/wiki/Wikipedia:Your_first_article'), ('Nominate an article', 'https://en.wikipedia.org/wiki/Template_talk:Did_you_know'), ('poisoning of Sergei Skripal', 'https://en.wikipedia.org/wiki/Poisoning_of_Sergei_and_Yulia_Skripal'), ('nerve agent', 'https://en.wikipedia.org/wiki/Nerve_agent'), ('Stephen Hawking', 'https://en.wikipedia.org/wiki/Stephen_Hawking'), ('US-Bangla Airlines Flight 211', 'https://en.wikipedia.org/wiki/US-Bangla_Airlines_Flight_211'), ('Dhaka', 'https://en.wikipedia.org/wiki/Dhaka'), ('Kathmandu', 'https://en.wikipedia.org/wiki/Kathmandu'), ('Winter Paralympics', 'https://en.wikipedia.org/wiki/2018_Winter_Paralympics'), ('Pyeongchang', 'https://en.wikipedia.org/wiki/Pyeongchang_County'), ('USS Lexington', 'https://en.wikipedia.org/wiki/USS_Lexington_(CV-2)'), ('Coral Sea', 'https://en.wikipedia.org/wiki/Coral_Sea'), ('Ongoing', 'https://en.wikipedia.org/wiki/Portal:Current_events'), ('Rif Dimashq offensive', 'https://en.wikipedia.org/wiki/Rif_Dimashq_offensive_(February_2018%E2%80%93present)'), ('Turkish military operation in Afrin', 'https://en.wikipedia.org/wiki/Turkish_military_operation_in_Afrin'), ('Recent deaths', 'https://en.wikipedia.org/wiki/Deaths_in_2018'), ('Jim Bowen', 'https://en.wikipedia.org/wiki/Jim_Bowen'), ('Ken Dodd', 'https://en.wikipedia.org/wiki/Ken_Dodd'), ('Karl Lehmann', 'https://en.wikipedia.org/wiki/Karl_Lehmann'), ('Millie Dunn Veasey', 'https://en.wikipedia.org/wiki/Millie_Dunn_Veasey'), ('Nominate an article', 'https://en.wikipedia.org/wiki/Wikipedia:In_the_news/Candidates'), ('March 16', 'https://en.wikipedia.org/wiki/March_16'), ('1621', 'https://en.wikipedia.org/wiki/1621'), ('Samoset', 'https://en.wikipedia.org/wiki/Samoset'), ('Abenaki', 'https://en.wikipedia.org/wiki/Abenaki'), ('Plymouth Colony', 'https://en.wikipedia.org/wiki/Plymouth_Colony'), ('Pilgrims', 'https://en.wikipedia.org/wiki/Pilgrims_(Plymouth_Colony)'), ('1689', 'https://en.wikipedia.org/wiki/1689'), ('Royal Welch Fusiliers', 'https://en.wikipedia.org/wiki/Royal_Welch_Fusiliers'), ('line infantry', 'https://en.wikipedia.org/wiki/Line_infantry'), ('British Army', 'https://en.wikipedia.org/wiki/British_Army'), ('1918', 'https://en.wikipedia.org/wiki/1918'), ('Finnish Civil War', 'https://en.wikipedia.org/wiki/Finnish_Civil_War'), ('Whites', 'https://en.wikipedia.org/wiki/Whites_(Finland)'), ('Battle of L?0?1nkipohja', 'https://en.wikipedia.org/wiki/Battle_of_L%C3%A4nkipohja'), ('Reds', 'https://en.wikipedia.org/wiki/Finnish_Socialist_Workers%27_Republic'), ('1988', 'https://en.wikipedia.org/wiki/1988'), ('loyalist', 'https://en.wikipedia.org/wiki/Ulster_loyalism'), ('Michael Stone', 'https://en.wikipedia.org/wiki/Michael_Stone_(loyalist)'), ('attacked', 'https://en.wikipedia.org/wiki/Milltown_Cemetery_attack'), ('Provisional IRA', 'https://en.wikipedia.org/wiki/Provisional_Irish_Republican_Army'), ('killed in Gibraltar', 'https://en.wikipedia.org/wiki/Operation_Flavius'), ('2014', 'https://en.wikipedia.org/wiki/2014'), ('Annexation of Crimea', 'https://en.wikipedia.org/wiki/Annexation_of_Crimea_by_the_Russian_Federation'), ('Autonomous Republic of Crimea', 'https://en.wikipedia.org/wiki/Autonomous_Republic_of_Crimea'), ('a controversial referendum', 'https://en.wikipedia.org/wiki/Crimean_status_referendum,_2014'), ('federal subject', 'https://en.wikipedia.org/wiki/Federal_subjects_of_Russia'), ('Caroline Herschel', 'https://en.wikipedia.org/wiki/Caroline_Herschel'), ('Iso Rae', 'https://en.wikipedia.org/wiki/Iso_Rae'), ('Mary Meader', 'https://en.wikipedia.org/wiki/Mary_Meader'), ('March 15', 'https://en.wikipedia.org/wiki/March_15'), ('March 16', 'https://en.wikipedia.org/wiki/March_16'), ('March 17', 'https://en.wikipedia.org/wiki/March_17'), ('Archive', 'https://en.wikipedia.org/wiki/Wikipedia:Selected_anniversaries/March'), ('List of historical anniversaries', 'https://en.wikipedia.org/wiki/List_of_historical_anniversaries'), ('Laureus World Sports Award for Sportswoman of the Year', 'https://en.wikipedia.org/wiki/Laureus_World_Sports_Award_for_Sportswoman_of_the_Year'), ('Laureus World Sports Awards', 'https://en.wikipedia.org/wiki/Laureus_World_Sports_Awards'), ('Cartier', 'https://en.wikipedia.org/wiki/Cartier_(jeweler)'), ('Serena Williams', 'https://en.wikipedia.org/wiki/Serena_Williams'), ('Full\xa0list...', 'https://en.wikipedia.org/wiki/Laureus_World_Sports_Award_for_Sportswoman_of_the_Year'), ('Transformers: Robots in Disguise (2015 TV series) episodes', 'https://en.wikipedia.org/wiki/List_of_Transformers:_Robots_in_Disguise_(2015_TV_series)_episodes'), ('Works by Georgette Heyer', 'https://en.wikipedia.org/wiki/List_of_works_by_Georgette_Heyer'), ('70th Academy Awards', 'https://en.wikipedia.org/wiki/70th_Academy_Awards'), ('Archive', 'https://en.wikipedia.org/wiki/Wikipedia:Today%27s_featured_list/March_2018'), ('More featured lists', 'https://en.wikipedia.org/wiki/Wikipedia:Featured_lists'), ('Interior with Young Woman Seen from the Back', 'https://en.wikipedia.org/wiki/Interior_with_Young_Woman_Seen_from_the_Back'), ('oil painting', 'https://en.wikipedia.org/wiki/Oil_painting'), ('Vilhelm Hammersh?0?3i', 'https://en.wikipedia.org/wiki/Vilhelm_Hammersh%C3%B8i'), ('Randers Museum of Art', 'https://en.wikipedia.org/wiki/Randers_Museum_of_Art'), ('Randers', 'https://en.wikipedia.org/wiki/Randers'), ('Vilhelm Hammersh?0?3i', 'https://en.wikipedia.org/wiki/Vilhelm_Hammersh%C3%B8i'), ('H?0?2s?0?2k tere', 'https://en.wikipedia.org/wiki/Template:POTD/2018-03-15'), ('Albert Bridge, London', 'https://en.wikipedia.org/wiki/Template:POTD/2018-03-14'), ('Polypogon monspeliensis', 'https://en.wikipedia.org/wiki/Template:POTD/2018-03-13'), ('Archive', 'https://en.wikipedia.org/wiki/Wikipedia:Picture_of_the_day/March_2018'), ('More featured pictures', 'https://en.wikipedia.org/wiki/Wikipedia:Featured_pictures'), ('Community portal', 'https://en.wikipedia.org/wiki/Wikipedia:Community_portal'), ('Help desk', 'https://en.wikipedia.org/wiki/Wikipedia:Help_desk'), ('Local embassy', 'https://en.wikipedia.org/wiki/Wikipedia:Local_Embassy'), ('Reference desk', 'https://en.wikipedia.org/wiki/Wikipedia:Reference_desk'), ('Site news', 'https://en.wikipedia.org/wiki/Wikipedia:News'), ('Village pump', 'https://en.wikipedia.org/wiki/Wikipedia:Village_pump'), ('Wikimedia Foundation', 'https://en.wikipedia.org/wiki/Wikimedia_Foundation'), ('English', 'https://en.wikipedia.org/wiki/English_language'), ('5,590,367', 'https://en.wikipedia.org/wiki/Special:Statistics'), ('Talk', 'https://en.wikipedia.org/wiki/Special:MyTalk'), ('Contributions', 'https://en.wikipedia.org/wiki/Special:MyContributions'), ('Main Page', 'https://en.wikipedia.org/wiki/Main_Page'), ('Talk', 'https://en.wikipedia.org/wiki/Talk:Main_Page'), ('Read', 'https://en.wikipedia.org/wiki/Main_Page'), ('', 'https://en.wikipedia.org/wiki/Main_Page'), ('Main page', 'https://en.wikipedia.org/wiki/Main_Page'), ('Contents', 'https://en.wikipedia.org/wiki/Portal:Contents'), ('Featured content', 'https://en.wikipedia.org/wiki/Portal:Featured_content'), ('Current events', 'https://en.wikipedia.org/wiki/Portal:Current_events'), ('Random article', 'https://en.wikipedia.org/wiki/Special:Random'), ('Help', 'https://en.wikipedia.org/wiki/Help:Contents'), ('About Wikipedia', 'https://en.wikipedia.org/wiki/Wikipedia:About'), ('Community portal', 'https://en.wikipedia.org/wiki/Wikipedia:Community_portal'), ('Recent changes', 'https://en.wikipedia.org/wiki/Special:RecentChanges'), ('What links here', 'https://en.wikipedia.org/wiki/Special:WhatLinksHere/Main_Page'), ('Related changes', 'https://en.wikipedia.org/wiki/Special:RecentChangesLinked/Main_Page'), ('Upload file', 'https://en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard'), ('Special pages', 'https://en.wikipedia.org/wiki/Special:SpecialPages'), ('About Wikipedia', 'https://en.wikipedia.org/wiki/Wikipedia:About'), ('Disclaimers', 'https://en.wikipedia.org/wiki/Wikipedia:General_disclaimer'))
        
finally:
    cursor.close()
    connection.close()
