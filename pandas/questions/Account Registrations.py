https://platform.stratascratch.com/coding/2126-account-registrations?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = noom_signups
df['started_at'] = df['started_at'].dt.strftime("%Y-%m")
df.groupby('started_at').agg({'signup_id':'count'}).reset_index()
