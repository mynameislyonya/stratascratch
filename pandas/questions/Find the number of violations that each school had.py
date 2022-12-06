https://platform.stratascratch.com/coding/9727-find-the-number-of-violations-that-each-school-had?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = sf_restaurant_health_violations
df['risk_category'] = df.risk_category.fillna(0)
df['business_name']= df['business_name'].apply(lambda x:x.lower())
df[(df.risk_category !=0) & (df['business_name'].str.contains('school'))].groupby('business_name').agg({'inspection_id':'count'}).reset_index()
