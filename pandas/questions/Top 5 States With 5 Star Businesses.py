https://platform.stratascratch.com/coding/10046-top-5-states-with-5-star-businesses?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = yelp_business
df = df[df.stars == 5]
df =df.groupby('state').agg({'business_id':'count'}).reset_index()
df['rank'] = df['business_id'].rank(method='min', ascending=False)
df[df['rank'] < 6]
