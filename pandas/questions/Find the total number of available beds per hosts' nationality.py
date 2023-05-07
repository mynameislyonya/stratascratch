https://platform.stratascratch.com/coding/10187-find-the-total-number-of-available-beds-per-hosts-nationality?code_type=2
  
# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(airbnb_apartments,airbnb_hosts, on='host_id').groupby('nationality')['n_beds'].sum().reset_index().sort_values('n_beds',ascending= False)
