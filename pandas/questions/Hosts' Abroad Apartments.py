https://platform.stratascratch.com/coding/10071-hosts-abroad-apartments?code_type=2
  
# Import your libraries
import pandas as pd

# Start writing code
merged = pd.merge(airbnb_hosts, airbnb_apartments, on = "host_id")
new = merged[merged["nationality"] != merged["country"]]
result = new["host_id"].nunique()
