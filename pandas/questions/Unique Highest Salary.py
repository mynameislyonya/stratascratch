https://platform.stratascratch.com/coding/9919-unique-highest-salary?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = employee
df = df.groupby('salary').agg({'id':'count'}).reset_index().sort_values(by = 'id',ascending = False)
df[df.id == 1].sort_values(by ='salary').tail(1)
