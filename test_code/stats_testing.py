import pandas as pd
import numpy as np

df = pd.read_excel('stats_correlation_test.xlsx')

print(df)

column = df['NPI-Value'].tolist()

column2 = df['Group (Maintenance) Topic: Speed efficiency'].tolist()

print(column[0])

print(np.corrcoef(column, column2)[0, 1])

