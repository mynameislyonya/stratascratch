https://platform.stratascratch.com/coding/10161-ranking-hosts-by-beds?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code
n = airbnb_apartments.groupby('host_id')['n_beds'].sum().to_frame('number_of_beds').reset_index()

n['rank'] = n['number_of_beds'].rank(method = 'dense',ascending = False)
n.sort_values(by='rank')
