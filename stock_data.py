import yfinance as yf
import pandas as pd
import requests
import json

#Get data
r = requests.get('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json')
s = requests.get('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json')

apple = yf.Ticker("AAPL")
amd = yf.Ticker("AMD")

with open(r'D:\OneDrive - APL Logistics Ltd\Documents\Git\DS\apple.json','r') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
apple_info

with open(r'D:\OneDrive - APL Logistics Ltd\Documents\Git\DS\amd.json','r') as json_file1:
    amd_info = json.load(json_file1)
    # Print the type of data variable    
amd_info

# Checking the country
apple_info['country'] 
amd_info['country']

# Checking the history
apple_share_price_data = apple.history(period="max")
amd_share_price_data = apple.history(period="max")
apple_share_price_data.head()
amd_share_price_data.head()

#reset the dataframe index
apple_share_price_data.reset_index(inplace=True)
amd_share_price_data.reset_index(inplace=True) 

# Plot the history price data
apple_share_price_data.plot(x="Date", y="Open") # Plot the opening price
apple_share_price_data.plot(x="Date", y="High") # Plot the high price
apple_share_price_data.plot(x="Date", y="Low") # Plot the low price
apple_share_price_data.plot(x="Date", y="Close") # Plot the closing price

amd_share_price_data.plot(x="Date", y="Open") # Plot the opening price
amd_share_price_data.plot(x="Date", y="High") # Plot the high price
amd_share_price_data.plot(x="Date", y="Low") # Plot the low price
amd_share_price_data.plot(x="Date", y="Close") # Plot the closing price

# Check the dividends
apple.dividends
amd.dividends