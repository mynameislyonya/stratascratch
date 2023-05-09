https://platform.stratascratch.com/coding/9878-countries-with-most-negative-reviews?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = hotel_reviews[~hotel_reviews['negative_review'].str.contains('No Negative')]
df.groupby('reviewer_nationality')['negative_review'].count().rename('n_cnt').reset_index()
