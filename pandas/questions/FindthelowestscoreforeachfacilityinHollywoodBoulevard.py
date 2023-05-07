https://platform.stratascratch.com/coding/10180-find-the-lowest-score-for-each-facility-in-hollywood-boulevard?code_type=2

# Import your libraries
import pandas as pd

filtered = los_angeles_restaurant_health_inspections[los_angeles_restaurant_health_inspections.facility_address.str.contains("HOLLYWOOD BLVD")]
result = filtered.groupby("facility_name").score.min().to_frame("min_score").reset_index().sort_values(by=["min_score", "facility_name"], ascending=[False, True])
