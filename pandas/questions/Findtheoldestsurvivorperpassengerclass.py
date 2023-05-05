https://platform.stratascratch.com/coding/9883-find-the-oldest-survivor-per-passenger-class?code_type=2
  
  # Import your libraries
import pandas as pd

# Start writing code
df=titanic
df=df[df['survived']==1]
p_ages=df.groupby('pclass')['age'].max()
df=pd.merge(p_ages,df,on=['pclass','age'])[['pclass','name','age']]
df.sort_values('age')
