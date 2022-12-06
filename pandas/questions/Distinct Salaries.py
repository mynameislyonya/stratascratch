https://platform.stratascratch.com/coding/9898-unique-salaries?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
distinct = twitter_employee.drop_duplicates(subset = ['department','salary'])
top3 = distinct.groupby(['department'])['salary'].nlargest(3).to_frame().reset_index()

top3[['department','salary']]
