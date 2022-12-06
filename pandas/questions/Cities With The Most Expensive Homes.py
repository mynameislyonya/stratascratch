https://platform.stratascratch.com/coding/10315-cities-with-the-most-expensive-homes?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = zillow_transactions
md = df.mkt_price.mean()
df = df.groupby('city').agg({'mkt_price':'mean'}).reset_index()
df[df.mkt_price>md]
