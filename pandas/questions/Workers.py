https://platform.stratascratch.com/coding/10152-workers-with-the-highest-and-lowest-salaries/solutions?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
worker['highest_sal'] = worker['salary'].rank(method='dense', ascending=False)
worker['lowest_sal'] = worker['salary'].rank(method='dense', ascending=True)
worker = worker[(worker['highest_sal'] == 1) | (worker['lowest_sal'] == 1)]
worker.loc[worker['highest_sal']==1, 'salary_type'] = 'Highest Salary'
worker.loc[worker['lowest_sal']==1, 'salary_type'] = 'Lowest Salary'
res = worker[["worker_id", "salary", "department", "salary_type"]]
