https://platform.stratascratch.com/coding/10053-most-checkins?code_type=2
  
# Import your libraries
import pandas as pd

# Start writing code
yelp_checkin.sort_values('checkins',ascending=False)[['business_id','checkins']].head(5)
