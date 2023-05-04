https://platform.stratascratch.com/coding/2124-top-two-media-types/solutions?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
facebook_sales_promotions.head()
df = facebook_sales_promotions
df.groupby('media_type').cost.sum().reset_index().sort_values('cost', ascending = False).head(2)
