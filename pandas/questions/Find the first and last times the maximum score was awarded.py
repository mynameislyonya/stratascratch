https://platform.stratascratch.com/coding/9712-find-the-first-and-last-times-the-maximum-score-was-awarded?code_type=2
  
 # Import your libraries
import pandas as pd

# Start writing code
df = los_angeles_restaurant_health_inspections
df = df[df['score'] == df['score'].max()]
dfmx = df[df['activity_date'] == df['activity_date'].max()]['activity_date'].dt.date.to_frame('mx').reset_index(0)
dfmn = df[df['activity_date'] == df['activity_date'].min()]['activity_date'].dt.date.to_frame('mn').reset_index(0)
df = pd.concat([dfmx,dfmn],axis=1)
df[['mx','mn']]
