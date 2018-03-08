import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


forex_11 = pd.read_csv('FOREX_20180111.csv', sep=',', parse_dates=['Date'])
forex_12 = pd.read_csv('FOREX_20180112.csv', sep=',', parse_dates=['Date'])
time_format = '%d-%m-%Y'

forex = forex_11.append(forex_12, ignore_index=False)
forex['Date'] = forex['Date'].dt.strftime(time_format)
# print(forex)
forex = forex.reset_index(drop=True)
forex = forex.loc[forex.groupby("Symbol")["Open"].idxmax()]
# forex = forex.drop_duplicates(subset=['Symbol'], keep='first', inplace=False)
print(forex)
print(forex[forex['Date']== '12-01-2018'])
