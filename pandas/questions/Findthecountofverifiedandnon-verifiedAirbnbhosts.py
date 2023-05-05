https://platform.stratascratch.com/coding/9629-find-the-count-of-verified-and-non-verified-airbnb-hosts?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details.groupby(by = 'host_identity_verified')['id'].count().to_frame().reset_index()
