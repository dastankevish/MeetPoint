import aiohttp

from .all_airports import Airport


async def get_international_airports_rowids(sql_session):
    async with aiohttp.ClientSession() as http_session:
        #rowid_len = cursor.execute(f"SELECT rowid FROM all_airports_info")
        #rowid_len = len(cursor.fetchall())
        rowid_len = session.query(Airport)
        
        tasks = []
        wiki_checklist = []
        name_checklist = []
        result = []
        
        for rowid in range(1, rowid_len+1):
            row = cursor.execute(f"SELECT * FROM all_airports_info WHERE rowid={rowid}")
            row = cursor.fetchone()
            
            wiki_check = True 
            db_name = None
            
            #row[-1] == '':
            if row[-1] != '':
                name = row[-1].split('/')[-1].replace('_', ' ') # name of airport
            else:
                name = row[1]
            
            for word in name.split():
                if word.lower().find('regional') != -1:
                    wiki_check = False
                    break
            
                if word.lower().find('international') != -1:
                    wiki_check = False
                    name_checklist.append(rowid)
                    break
                
                name = name.replace(' ', '_')
            
            if wiki_check == True:
                task = asyncio.create_task(request_wiki(http_session, rowid, name))
                tasks.append(task)
            
            if len(tasks) == 100:
                wiki_checklist += await asyncio.gather(*tasks)
                tasks = []
                
        wiki_checklist += await asyncio.gather(*tasks)
    
    for _ in range(len(wiki_checklist)):
        if wiki_checklist[_] != None:
            result.append(wiki_checklist[_])
        
    result += name_checklist
    return result
