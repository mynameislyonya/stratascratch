https://platform.stratascratch.com/coding/2019-top-2-users-with-most-calls?code_type=2
  
# Import your libraries
import pandas as pd

# Start writing code
merged = pd.merge(rc_calls, rc_users, on = 'user_id', how = 'left')
prerank = merged.groupby(['company_id', 'user_id'])['call_id'].count().to_frame('no_calls').reset_index()
prerank['rank'] = prerank.groupby('company_id')['no_calls'].rank(method = 'dense', ascending = False)
result = prerank[prerank['rank'] <= 2]
