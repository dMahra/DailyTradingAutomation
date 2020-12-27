# SystemStockAutomation
Automated a  
# Download Signals
This script downloads trade signals from a subscription based signal system(Vistalytics). The signal file is downloaded using HTTP protocol. Includes authentication(userID + password). This file is saved in user's local directory(Downloads). The signal file contains stock ticker and either a buy, hold or sell signal. It doesn't, however, have price or quantity recorded. It's for the individual subscriber to determine the quantity according to the trading capital in play.  
# Generate Trade Files
Here we merge our signal file with another .csv(from Yahoo) that contains respective price(end of day closed) and quantity. The merge file contains the format needed required by Interactive Broker when we submit our requests before the market opens. Format: Date, Stock, Signal, Price, Quantity. 
# Submit Trades
This script submits trades to Interative Broker through IB APIs. All trades are MKT. 
