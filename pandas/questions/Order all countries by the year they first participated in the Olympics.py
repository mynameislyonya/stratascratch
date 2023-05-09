https://platform.stratascratch.com/coding/10184-order-all-countries-by-the-year-they-first-participated-in-the-olympics?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
oae = olympics_athletes_events

oae.groupby(['noc'])['year'].min().to_frame('first_time_year').reset_index().sort_values(['first_time_year'])
