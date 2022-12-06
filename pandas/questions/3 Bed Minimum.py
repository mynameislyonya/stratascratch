https://platform.stratascratch.com/coding/9627-3-bed-minimum?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code
min_beds = airbnb_search_details.groupby(['neighbourhood']).filter(lambda g: sum(g['beds']) >= 3).groupby('neighbourhood').mean().reset_index()
