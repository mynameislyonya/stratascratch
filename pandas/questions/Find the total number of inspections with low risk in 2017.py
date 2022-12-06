https://platform.stratascratch.com/coding/9705-find-the-total-number-of-inspections-with-low-risk-in-2017?code_type=2
  
 import pandas as pd
import numpy as np

low_2017 = los_angeles_restaurant_health_inspections[(los_angeles_restaurant_health_inspections['pe_description'].astype(str).str.contains('LOW')) & (los_angeles_restaurant_health_inspections['activity_date'].astype(str).str.contains('2017'))]
result = len(low_2017)
