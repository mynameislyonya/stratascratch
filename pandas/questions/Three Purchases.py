https://platform.stratascratch.com/coding/2095-three-purchases?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code
df = amazon_orders
df['year'] = df['order_date'].dt.year
df20 = df[df.year==2020].groupby('user_id').filter(lambda x: len(x) >= 3)
df21 = df[df.year==2021].groupby('user_id').filter(lambda x: len(x) >= 3)
df = df20.merge(df21, how='inner', on='user_id')
df['user_id'].drop_duplicates()
