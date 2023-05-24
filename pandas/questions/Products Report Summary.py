https://platform.stratascratch.com/coding/2039-products-report-summary?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
wfm_transactions.head()

merged_wfm = wfm_transactions.merge(wfm_products, on = 'product_id')
merged_wfm = merged_wfm[merged_wfm['transaction_date'].dt.year == 2017]
merged_wfm.groupby('product_category').agg({'transaction_id':'nunique', 'sales':'sum'}).reset_index().sort_values('sales', ascending = False)
