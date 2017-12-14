import sched, time, requests, pymongo, pprint, json
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
    passedData.insert(1, requests.get(url=baseURL+"ltc_btc").json() )
    passedData.insert(2, requests.get(url=baseURL+"btc_usd").json() )
    passedData.insert(3, requests.get(url=baseURL+"ltc_usd").json() )
    passedData.insert(4, requests.get(url=baseURL+"bch_btc").json() )
    passedData.insert(5, requests.get(url=baseURL+"bch_usd").json() )
    print(passedData)
    #for i in passedData:
        #json.loads(passedData[i].get_content_charset('utf-8'))
        #passedData[i] = passedData[i].replace("'","")

    #results = posts.insert_many(passedData);
    #pprint(results.inserted_ids)
scheduler.enter(2,1,get_prices,(scheduler,))
print("requesting Data: ")
scheduler.run();
