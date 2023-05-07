https://platform.stratascratch.com/coding/10083-start-dates-of-top-drivers?code_type=2
  
# Import your libraries
import pandas as pd

# Start writing code
df = lyft_drivers

df = df[df['end_date'].isnull()].sort_values(['yearly_salary'], ascending = False).head()
