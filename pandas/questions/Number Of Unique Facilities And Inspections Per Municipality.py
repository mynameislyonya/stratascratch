https://platform.stratascratch.com/coding/9702-number-of-unique-facilities-and-inspections-per-municipality?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = los_angeles_restaurant_health_inspections
df.groupby('facility_zip').agg({'facility_id':pd.Series.nunique,'record_id':'count'}).reset_index().sort_values(by = 'record_id',ascending=False)
