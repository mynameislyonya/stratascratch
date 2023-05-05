https://platform.stratascratch.com/coding/9661-find-the-student-with-the-highest-efficiency-for-mathematics?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
sat_scores.head()
sat_scores = sat_scores[(sat_scores['hrs_studied'] > 0)]
sat_scores['efficiency'] = sat_scores['sat_math'] / sat_scores['hrs_studied']
sat_scores.sort_values('efficiency', ascending=False).head(1)[['student_id', 'hrs_studied', 'sat_math', 'efficiency']]
