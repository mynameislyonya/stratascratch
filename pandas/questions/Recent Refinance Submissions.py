https://platform.stratascratch.com/coding/2003-recent-refinance-submissions?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code


loans = loans[loans['type'] == 'Refinance']
loans['rnk'] = loans.groupby('user_id')['created_at'].rank(method = 'first', ascending = False)
loans = loans[loans['rnk'] == 1]
merged = loans.merge(submissions, left_on = 'id', right_on = 'loan_id', how = 'inner')
result = merged[['user_id', 'balance']]
