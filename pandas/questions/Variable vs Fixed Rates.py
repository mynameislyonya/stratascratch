https://platform.stratascratch.com/coding/2000-variable-vs-fixed-rates?code_type=2

# Import your libraries
import pandas as pd

# Start writing code

result = submissions.groupby(['loan_id', 'rate_type'])['id'].count().unstack(level=1).fillna(0).reset_index()
