https://platform.stratascratch.com/coding/9876-find-the-top-ten-hotels-with-the-most-negative-reviews-in-summer-june-aug?code_type=2
  
# Import your libraries
import pandas as pd

# Start writing code
hotel_reviews.head()

hotel_reviews=hotel_reviews[hotel_reviews.negative_review!='No Negative']
hotel_reviews.groupby('hotel_name').review_date.count().reset_index().sort_values('review_date',ascending=False).nlargest(2,'review_date')
