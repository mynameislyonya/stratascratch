https://platform.stratascratch.com/coding/10013-positive-ad-channels?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
uber_advertising.head()

df = uber_advertising[uber_advertising['customers_acquired'] > 1500]
df_2 = df.groupby('advertising_channel')['money_spent'].max().reset_index()
df_2['rank'] =  df_2['money_spent'].rank(method='min', ascending=True)
df_2[df_2['rank'] ==1]['advertising_channel']
