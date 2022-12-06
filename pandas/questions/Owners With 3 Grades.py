https://platform.stratascratch.com/coding/9710-owners-with-3-grades?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code
df = la_restaurant_health_inspections
df = df.groupby(['owner_name','facility_name'])['grade'].nunique().reset_index()
df[df.grade==3]
