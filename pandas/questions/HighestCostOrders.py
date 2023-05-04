

# Import your libraries
import pandas as pd

# Start writing code
df = orders.merge(customers, left_on='cust_id', right_on='id')
df = df[df['order_date'].between('2019-02-01', '2019-05-01')]
df = df.groupby(['first_name', 'order_date'], as_index=False)['total_order_cost'].sum()
df.nlargest(1, 'total_order_cost')
