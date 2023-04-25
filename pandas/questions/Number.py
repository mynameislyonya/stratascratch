https://platform.stratascratch.com/coding/10120-number-of-custom-email-labels/solutions?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(google_gmail_emails, google_gmail_labels, how='inner', left_on='id', right_on='email_id')
df = df[['to_user', 'label', 'id']] 
df = df[df['label'].str.contains('Custom')]
df = df.groupby(['to_user','label']).agg('count').reset_index()
df
