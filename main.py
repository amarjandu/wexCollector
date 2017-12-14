import sched, time, requests, pymongo, pprint, json
from pymongo import MongoClient



userName ='amar'
pwd ='thxadm1ns'
dbUrl = "mongodb://" + userName + ":" + pwd +  "@localhost/test"

client = MongoClient(dbUrl);

db = client['wexCollection']
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
    results = posts.insert_many(passedData);
    pprint.pprint(results.inserted_ids)
    scheduler.enter(2,1,get_prices,(sc,))

print("requesting Data: ")
scheduler.enter(2,1,get_prices,(scheduler,))
scheduler.run()
