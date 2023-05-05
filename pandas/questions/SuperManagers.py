https://platform.stratascratch.com/coding/9901-super-managers?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code
manager_df= employee.groupby('manager_id').size().reset_index()
super_managers = manager_df[manager_df[0] >= 7]['manager_id'].to_list()
df = employee[employee['id'].isin(super_managers)]['first_name']
