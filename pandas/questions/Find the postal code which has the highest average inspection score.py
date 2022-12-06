https://platform.stratascratch.com/coding/9724-find-the-postal-code-which-has-the-highest-average-inspection-score?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code
df = sf_restaurant_health_violations
df.groupby('business_postal_code').agg({'inspection_score':'mean'}).reset_index().sort_values(by = 'inspection_score').tail(1)
