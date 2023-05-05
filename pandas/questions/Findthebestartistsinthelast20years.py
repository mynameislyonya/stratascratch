https://platform.stratascratch.com/coding/9745-find-the-best-artists-in-the-last-50-years/solutions?code_type=2

import pandas as pd
import numpy as np
from datetime import datetime

billboard_top_100_year_end['year_diff'] = datetime.now().year - billboard_top_100_year_end['year']
df = billboard_top_100_year_end[billboard_top_100_year_end['year_diff'] <= 20]
grouped = df.groupby(['artist']).agg({'year_rank':'mean', 'year':'nunique'}).reset_index().rename(columns={"year_rank": "average_rank","year": "years_present"})
grouped['score'] = ((100 - grouped['average_rank']) * grouped['years_present']).round(2)
grouped['average_rank'] = grouped['average_rank'].round(2)
result = grouped.sort_values('score', ascending = False)
