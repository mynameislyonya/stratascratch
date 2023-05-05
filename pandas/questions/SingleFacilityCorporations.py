https://platform.stratascratch.com/coding/9694-single-facility-corporations?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = los_angeles_restaurant_health_inspections
df = df.groupby(['owner_name', 'owner_id'])['facility_id'].nunique().reset_index()
df[df['facility_id'] == 1]
