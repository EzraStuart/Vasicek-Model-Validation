import pandas as pd
from fredapi import Fred

fred = Fred(api_key = 'd037bfcdecb3cc2ada8463016b6bec52')

series_ids = ['DGS1MO','DGS3MO','DGS6MO','DGS1','DGS2','DGS5','DGS10','DGS30']

yields = pd.concat([fred.get_series(sid).rename(sid) for sid in series_ids], axis = 1)
yield_10y = fred.get_series('DGS10')
yield_30y = fred.get_series('DGS30')
yield_10y.index.name = 'Date'
yield_30y.index.name = 'Date'
yields.index.name = 'Date'

df = yield_10y.to_frame(name='rates')

df.index.name = 'Date'
df = df.loc['1990-01-01':'2025-10-15']

df_monthly = df.resample('ME').last()

df_monthly.to_csv('10_year_yields.csv')

