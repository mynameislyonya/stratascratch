https://platform.stratascratch.com/coding/2075-homework-results?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
allstate_homework.head()
new = pd.merge(allstate_homework,allstate_students)
new['completed']=new['grade'].notna()
new
df = new.groupby(['student_id','student_firstname'])[['grade','completed']].mean().reset_index()
df['completed'] =df['completed']*100
df
