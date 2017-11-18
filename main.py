import sched, time, urllib.request, pymongo, pprint, json 
from pymongo import MongoClient



userName ='amar'
pwd ='thxadm1ns'
dbUrl = "mongodb://" + userName + ":" + pwd +  "@localhost/wexCollbection"

print(dbUrl)                    
client = MongoClient(dbUrl); 
                     
db = client.wexCollection
posts = db.posts

baseURL = "https://wex.nz/api/3/ticker/"
passedData = []

scheduler = sched.scheduler(time.time, time.sleep)
def get_prices(sc):
    passedData.insert(1, urllib.request.urlopen(baseURL+"ltc_btc").read().decode('utf_8'))
    passedData.insert(2, urllib.request.urlopen(baseURL+"btc_usd").read().decode('utf_8'))
    passedData.insert(3, urllib.request.urlopen(baseURL+"ltc_usd").read().decode('utf_8'))
    for i in passedData:
        passedData[i] = passedData[i].replace("'","")
    
    #results = posts.insert_many(passedData);
    #pprint(results.inserted_ids)
    pprint.pprint(passedData)
        

    
scheduler.enter(2,1,get_prices,(scheduler,))
print("requesting Data: ")
scheduler.run();
