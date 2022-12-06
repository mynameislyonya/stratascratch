https://platform.stratascratch.com/coding/10318-new-products?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
car_launches.head()

df_2020 = car_launches[car_launches['year'].astype(str) == '2020']
df_2019 = car_launches[car_launches['year'].astype(str) == '2019']

df_2020 = df_2020.groupby('company_name').agg({'product_name':'count'}).reset_index()
df_2019 = df_2019.groupby('company_name').agg({'product_name':'count'}).reset_index()

df = df_2020.merge(df_2019, how='left', on='company_name')
df['diff'] = df['product_name_x'] - df['product_name_y']
df[['company_name','diff']]
