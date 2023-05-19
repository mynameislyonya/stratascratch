https://platform.stratascratch.com/coding/9682-find-industries-with-the-lowest-sales-but-still-makes-a-profit/solutions?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = forbes_global_2010_2014
df.groupby('industry').agg({'sales':'min','profits':'mean'}).reset_index().sort_values('sales',ascending=True)
