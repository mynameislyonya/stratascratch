https://platform.stratascratch.com/coding/9638-total-searches-for-rooms?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code
df = airbnb_search_details
df.groupby(['city','room_type']).agg({'id':'count'}).unstack(level=1).reset_index()
