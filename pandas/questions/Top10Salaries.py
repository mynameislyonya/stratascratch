https://platform.stratascratch.com/coding/9853-find-the-top-5-highest-salaries/solutions?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
worker['sal_rank'] = worker['salary'].rank(ascending=False, method='min')

worker[worker['sal_rank']<11][['worker_id','salary','department']].sort_values(by='salary',ascending=False)
