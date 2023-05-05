https://platform.stratascratch.com/coding/9619-find-the-search-details-for-villas-and-houses-with-wireless-internet-access/solutions?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_search_details[(airbnb_search_details['property_type'] == 'Villa') | (airbnb_search_details['property_type'] == 'House')]
df[df['amenities'].str.contains('"Wireless Internet"')]
