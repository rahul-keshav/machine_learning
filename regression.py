import pandas as pd
import quandl,math
import numpy as np
from sklearn import preprocessing,svm
from sklearn.model_selection import cross_val_score,cross_validate,train_test_split
from sklearn.linear_model import LinearRegression
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pickle
style.use('ggplot')


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
forecast_out=int(math.ceil(0.01*len(df)))


# the sheet is shifted upward means label shows the close price of 343 days later
# means price is increasing
df['label']=df[forcast_col].shift(-forecast_out)

df.dropna(inplace=True)

X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])
# y = y[:-forecast_out]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# clf=svm.SVR()
#
# clf=LinearRegression()
# clf.fit(X_train,y_train)
# with open('linearregression.pickle','wb') as f:
#     pickle.dump(clf, f)

pickle_in = open('linearregression.pickle','rb')
clf = pickle.load(pickle_in)

# accuracy=clf.score(X_test,y_test)

forecast_set=clf.predict(X_lately)

# print(forecast_set,accuracy,forecast_out)

df['Forecast']=np.nan

last_date=df.iloc[-1].name
last_unix=last_date.timestamp()
one_day=86400
next_unix=last_unix+one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()







