https://platform.stratascratch.com/coding/10351-activity-rank?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code
df = google_gmail_emails
df1 = df.groupby('from_user').agg({'day':'count'}).reset_index().rename(columns={'day':'cnt'})

df1['rank'] = df1.cnt.rank(method='first', ascending=False)
df1 = df1.sort_values(by=['rank', 'from_user'], ascending=[True, True])
