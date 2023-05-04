https://platform.stratascratch.com/coding/10039-macedonian-vintages/solutions?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df=winemag_p2
df=df[df['country']=='Macedonia']
df['year'] = df['title'].str.extract(r'(\d{4})')
df[['title','year']]
