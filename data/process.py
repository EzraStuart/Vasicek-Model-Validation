import pandas as pd

df = pd.read_csv('10_year_yields.csv', index_col='Date')

#df.index = pd.to_datetime(df.index)


calibration = df.loc['2004-12-31':'2019-12-31'].copy()
calibration['rates'] = calibration['rates'] /100
calibration.to_csv('calibration.csv')


# Holdout
holdout = df.loc['2019-12-01':'2025-10-15'].copy()
holdout['rates'] = holdout['rates'] /100
holdout.to_csv('holdout.csv')
