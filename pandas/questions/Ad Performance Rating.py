https://platform.stratascratch.com/coding/2155-ad-performance-rating/solutions?code_type=2

# Import your libraries
import pandas as pd

def my_function(x):
    if x > 30:
        return 'Outstanding'
    elif 20 <= x <= 30:
        return 'Satisfactory'
    elif 10 <= x <= 19:
        return 'Unsatisfactory'
    else:
        return 'Poor'
        
df = marketing_campaign
df = df.groupby('product_id')['quantity'].sum().reset_index()
df['ad_performance'] = df['quantity'].apply(my_function)
df
