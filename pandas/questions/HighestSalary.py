https://platform.stratascratch.com/coding/9870-highest-salary/solutions?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
max_salary = worker[worker.salary == worker.salary.max()][['first_name','salary']]
