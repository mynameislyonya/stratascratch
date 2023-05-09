https://platform.stratascratch.com/coding/9860-find-departments-with-less-than-4-employees?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code
worker.head()

worker = worker.groupby('department')['worker_id'].nunique().reset_index()

result = worker[worker['worker_id'] < 5]
