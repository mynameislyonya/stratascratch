https://platform.stratascratch.com/coding/9734-number-of-inspections-by-zip?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = sf_restaurant_health_violations
df['month'] = df['inspection_date'].dt.month
df['year'] = df['inspection_date'].dt.year
df[((df['month'] == 1) | (df['month'] == 5)  | (df['month'] ==11)) & (df.business_postal_code == 94102) ]\
.groupby(['year','month']).agg({'business_id':'count'}).unstack(level=1).fillna(0).reset_index()
