https://platform.stratascratch.com/coding/10035-find-the-number-of-wines-with-and-without-designations-per-country?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = winemag_p2
dfall = df.groupby('country').agg({'designation':'size'}).reset_index()
df['no']= df['designation'].isna().astype(int)
dfno = df.groupby('country').agg({'no':'sum'}).reset_index()
df = dfall.merge(dfno,how='left',on='country')
df['yes'] = df['designation'] - df['no']
df
