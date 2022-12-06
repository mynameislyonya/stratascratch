https://platform.stratascratch.com/coding/10043-median-price-of-wines?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
a = pd.concat([winemag_p1, winemag_p2],ignore_index=True)
a.groupby('variety').price.median().reset_index().drop_duplicates()
