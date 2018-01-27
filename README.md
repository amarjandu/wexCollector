# wexCollector
  This is a small part of a larger project that will be used to collect historical data from the exchange Wex.
  The project was started before TradingView was storing data for the Wex exchange, but it came out of neccessity due to
  lack of access to historical prices.
  
# Setup
  Need to create a mongoDB collection, specify it within the config, along with user and pwd for the database.
  Run main.py, ideally force it to run in the background, currently this is done with
  
  ````
   nohup python3 ./main.py &
    
  ````
  
  Ideally this should be moved to use something like supervisord to monitor and run the process. 
