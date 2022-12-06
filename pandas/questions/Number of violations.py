https://platform.stratascratch.com/coding/9728-inspections-that-resulted-in-violations?code_type=2
  
# Import your libraries
import pandas as pd

# Start writing code
df = sf_restaurant_health_violations
df['year'] = df['inspection_date'].dt.year
df['violation_id'] = df['violation_id'].dropna()
df[df.business_name == 'Roxanne Cafe'].groupby('year').violation_id.count().reset_index()
