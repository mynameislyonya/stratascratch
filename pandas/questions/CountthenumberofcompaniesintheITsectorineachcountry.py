https://platform.stratascratch.com/coding/9665-count-the-number-of-companies-in-the-it-sector-in-each-country/solutions?code_type=2

import pandas as pd
import numpy as np

df = forbes_global_2010_2014
result = df[df['sector'] == 'Information Technology'].groupby('country')['company'].size().reset_index(name='n_it_companies').sort_values('n_it_companies', ascending=False)
result
