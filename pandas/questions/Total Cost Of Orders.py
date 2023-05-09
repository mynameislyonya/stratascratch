https://platform.stratascratch.com/coding/10183-total-cost-of-orders?code_type=2
  
# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(orders, customers, how = 'left', left_on = 'cust_id', right_on = 'id')
df.groupby(['cust_id', 'first_name'])['total_order_cost'].sum().reset_index().sort_values('first_name')
