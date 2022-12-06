https://platform.stratascratch.com/coding/10049-reviews-of-categories?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = yelp_business
df['categories'] = df['categories'].apply(lambda x : x.split(';'))
df = df.explode('categories')

df.groupby('categories').agg({'review_count':'sum'}).reset_index().sort_values(by = 'review_count',ascending=False)
