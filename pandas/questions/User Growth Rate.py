https://platform.stratascratch.com/coding/2052-user-growth-rate?code_type=2
  
  # Import your libraries
import pandas as pd
import numpy as np

# Start writing code
sf_events.head()
df = sf_events
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df_2020 = df[(df.year == 2020) & (df.month == 12)].groupby('account_id').user_id.nunique().reset_index()
df_2021 = df[(df.year == 2021) & (df.month == 1)].groupby('account_id').user_id.nunique().reset_index()
df = df_2021.merge(df_2020, how='left', on='account_id')
df['rate'] = df.user_id_x/df.user_id_y
df[['account_id','rate']]
