https://platform.stratascratch.com/coding/2066-fastest-hometowns?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code
df = marathon_male
df = df.groupby('hometown').agg({'net_time':'mean'}).reset_index()
df['rnk']=df['net_time'].rank(method="dense",ascending=True)
df=df[df['rnk']<=3][['hometown','net_time']]
