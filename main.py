import sched, time, urllib.request
baseURL = "https://wex.nz/api/3/ticker/"
passedData = []

scheduler = sched.scheduler(time.time, time.sleep)
def get_prices(sc):
    passedData.insert(1, urllib.request.urlopen(baseURL+"ltc_btc").read() )
    passedData.insert(2, urllib.request.urlopen(baseURL+"btc_usd").read() )
    passedData.insert(3, urllib.request.urlopen(baseURL+"ltc_usd").read() )
    for i in passedData:
        print(i)
    scheduler.enter(2,1,get_prices, (sc,))

scheduler.enter(2,1,get_prices,(scheduler,))
print("requesting Data: ")
scheduler.run();
