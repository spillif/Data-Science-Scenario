import yfinance as yf
import pandas as pd
import requests

r = requests.get('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json')
print (r.json())

apple = yf.Ticker("AAPL")
print(apple)
