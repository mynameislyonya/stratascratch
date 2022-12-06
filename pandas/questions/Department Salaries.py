https://platform.stratascratch.com/coding/9921-department-salaries?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code
df1=employee[employee['sex']=='M'].groupby('department').agg({'id':'count','salary':'sum'}).reset_index().rename(columns={'id':'n_males','salary':'male_sal'})
df2=employee[employee['sex']=='F'].groupby('department').agg({'id':'count','salary':'sum'}).reset_index().rename(columns={'id':'n_females','salary':'female_sal','department':'department'})

df1.merge(df2, how='left', on='department')
