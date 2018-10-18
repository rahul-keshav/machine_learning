import pandas as pd
import quandl
import math

quandl.ApiConfig.api_key = "bvQnxeWtB1g8u_-FuwSk"
df =quandl.get('WIKI/GOOGL')
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT']=((df['Adj. High']-df['Adj. Close'])/df['Adj. Close'])*100
df['PCT_change']=((df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'])*100

df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forcast_col='Adj. Close'
df.fillna(-99999,inplace=True)

# print("length of df is",len(df))
# length of df is 3424
# so 0.1*len(df) gives 342.4 and after ceil it becomes 343
forcast_out=int(math.ceil(0.01*len(df)))


# the sheet is shifted upward means label shows the close price of 343 days later
# means price is increasing
df['label']=df[forcast_col].shift(-forcast_out)

df.dropna(inplace=True)

print("head",df.head())
print("tail",df.tail())





