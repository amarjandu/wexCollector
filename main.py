import sched, time, requests, pymongo, pprint, json, toml
from pymongo import MongoClient



configuration = toml.load('config/config.toml', _dict=dict)
dbUrl = "mongodb://" + configuration['mongoAuth']['Neptune']['userName'] + ":" + configuration['mongoAuth']['Neptune']['pwd'] +  "@localhost/admin"

client = MongoClient(dbUrl);
db = client[configuration['mongoConfig']['db']]
posts = db.configuration['mongoConfig']['collection']

baseURL = "https://wex.nz/api/3/ticker/"
passedData = []

scheduler = sched.scheduler(time.time, time.sleep)
def get_prices(sc):
    passedData.insert(1, requests.get(url=baseURL+"ltc_btc").json() )
    passedData.insert(2, requests.get(url=baseURL+"btc_usd").json() )
    passedData.insert(3, requests.get(url=baseURL+"ltc_usd").json() )
    passedData.insert(4, requests.get(url=baseURL+"bch_btc").json() )
    passedData.insert(5, requests.get(url=baseURL+"bch_usd").json() )
    results = posts.insert_many(passedData)
    pprint.pprint(results.inserted_ids)
    passedData.clear()
    scheduler.enter(configuration['scheduler']['secondDelay'],1,get_prices,(sc,))

print("requesting Data: ")
scheduler.enter(configuration['scheduler']['secondDelay'],1,get_prices,(scheduler,))
scheduler.run()
