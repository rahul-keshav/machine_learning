import pandas as pd
import quandl
quandl.ApiConfig.api_key = "bvQnxeWtB1g8u_-FuwSk"
df =quandl.get('WIKI/GOOGL')
print(df.head())



