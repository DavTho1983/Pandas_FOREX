import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(pd.__version__)

forex_11 = pd.read_csv('FOREX_20180111.csv', sep=',', parse_dates=['Date'])
forex_12 = pd.read_csv('FOREX_20180112.csv', sep=',', parse_dates=['Date'])
time_format = '%d-%m-%Y'
# print(forex.iloc[:5, :]) #first 5
# print(forex.iloc[-5:, :]) #last 5
# print(forex.head(2)) #first 2 rows
# print(forex.tail(2)) #last 2 rows

# print(forex.info())
#
# low = forex['Low']
# print(type(low))
# print(low.head())
#
# lows = low.values
# print(type(lows))
# print(lows[:5])

forex = forex_11.append(forex_12, ignore_index=False)
forex['Date'] = forex['Date'].dt.strftime(time_format)
# forex.index = [forex.index.strftime(time_format)]
GBP = forex[forex['Symbol'] == "GBPUSD"]
# forex.index = list(forex[['Date', 'Symbol']].itertuples(index=False, name=None))
tuples = list(forex[['Date', 'Symbol']].itertuples(index=False, name=None))
forex.index = pd.MultiIndex.from_tuples(tuples, names=['Date', 'Symbol'])
# print(forex.head())
# print(forex.tail())
# print(forex['Open'].tolist())


# print(GBP)
# print(forex.info())
# forex['Open'].plot() needs proper labels
# plt.show()
forex_open_close = pd.DataFrame(np.array(forex[['Open','Close']]), index=forex.index)
forex_open_close.columns = ['Open', 'Close']
forex_open_close['Day Change'] = forex_open_close['Close'] - forex_open_close['Open']
print(forex_open_close.head())
# print(forex_open_close.ix[[('11-01-2018', 'GBPUSD')]])
# print(forex_open_close.ix['11-01-2018', 'AEDCAD'])
idx = pd.IndexSlice
print(forex_open_close.loc[idx[:,['AUDARS']], :])

print(forex_open_close[(forex_open_close['Day Change'] > 0)].groupby('Symbol')['Day Change'].apply(list))
