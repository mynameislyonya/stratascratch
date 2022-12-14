https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=2

Find the titles of workers that earn the highest salary. Output the highest-paid title or multiple titles that share the highest salary.

import pandas as pd
title.rename(columns={'worker_ref_id':'worker_id'},inplace=True)
df = worker.merge(title,how='left',on='worker_id')
df[df.salary == df.salary.max()]['worker_title']
