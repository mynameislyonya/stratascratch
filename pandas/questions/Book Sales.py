https://platform.stratascratch.com/coding/2128-book-sales?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = amazon_books.merge(amazon_books_order_details,how='left', on='book_id')
df['quantity'] = df['quantity'].fillna(0)
df['total'] = df['quantity'] * df['unit_price']
df.groupby('book_id').agg({'total':'sum'}).reset_index()
