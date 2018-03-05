import pandas as pd

forex_11 = pd.read_csv('FOREX_20180111.csv', sep=',', parse_dates=['Date'], index_col=['Date'])
forex_12 = pd.read_csv('FOREX_20180112.csv', sep=',', parse_dates=['Date'], index_col=['Date'])
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
# forex['Date'] = forex['Date'].dt.strftime(time_format)
forex.index = forex.index.strftime(time_format)
print(forex.head())
print(forex.tail())

GBP = forex[forex['Symbol'] == "GBPUSD"]
print(GBP)
print(forex.info())
# print(forex.loc['January 11 2018':'January 12 2018'])
