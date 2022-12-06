https://platform.stratascratch.com/coding/9636-cheapest-neighborhoods-with-real-beds-and-internet?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code bed_type = 'Real Bed' and property_type = 'Villa' and amenities ilike '%Internet%'
df = airbnb_search_details
df[(df.bed_type == 'Real Bed') & (df.property_type == 'Villa') & (df.amenities.str.contains('Internet'))].sort_values(by = 'price').head(1)['neighbourhood']
