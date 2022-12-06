https://platform.stratascratch.com/coding/9729-inspections-per-risk-category?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code
df = sf_restaurant_health_violations
df['risk_category']=df['risk_category'].fillna(value='No Risk')
df.groupby('risk_category').inspection_id.nunique().reset_index()
