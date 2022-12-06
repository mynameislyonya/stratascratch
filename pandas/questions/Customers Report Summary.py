https://platform.stratascratch.com/coding/2040-customers-report-summary?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = wfm_transactions
df['year'] = df['transaction_date'].dt.year
df['month'] = df['transaction_date'].dt.month
df[(df['year']== 2017) & (df['sales']>=5)].groupby('month').agg({'customer_id':'nunique','transaction_id':'nunique'}).reset_index()
