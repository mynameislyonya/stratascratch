https://platform.stratascratch.com/coding/2098-world-tours?code_type=2

# Import your libraries
import pandas as pd

# Start writing cod
fd = travel_history
fd['r1'] = travel_history.groupby('traveler').date.rank(method='dense',ascending=False)
ff = fd[fd.r1 == 1]

fd['r2'] = travel_history.groupby('traveler').date.rank(method='dense',ascending=True)

ff2 = fd[fd.r2 == 1]

ff =ff.merge(ff2, how='left', on='traveler')
ff[ff['start_city_y'] == ff['end_city_x']].shape[0]
