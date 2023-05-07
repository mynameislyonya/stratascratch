https://platform.stratascratch.com/coding/10324-distances-traveled?code_type=2
  
# Import your libraries
import pandas as pd

# Start writing code
lyft_rides_log.head()
df=lyft_rides_log
df1=lyft_users
result=df.merge(df1,left_on='user_id',right_on='id',how='inner')
result.groupby(['user_id','name'])['distance'].sum().reset_index().nlargest(10,'distance')
