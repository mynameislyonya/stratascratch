https://platform.stratascratch.com/coding/2157-10-monthly-sales-increase/solutions?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = online_orders
df['date'] = df['date'].dt.month
df = df[df['date'].isin([4,5])]
df['total'] = df['units_sold'] * df['cost_in_dollars']
df =df.groupby(['date','product_id']).agg({'total':'sum'}).reset_index().sort_values('product_id')

df =df.pivot(index='product_id', columns='date', values='total').reset_index()
df.columns = ['product_id', 'april', 'may']
df = df[(df['april'].notnull())&(df['may'].notnull())]
df['perc'] = ((df['may'] - df['april'])/ df['april']) * 100
df[df['perc'] > 10][['product_id', 'perc']]
