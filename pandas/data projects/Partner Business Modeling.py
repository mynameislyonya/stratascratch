#!/usr/bin/env python
# coding: utf-8

# Scenario 1: It is going to be a huge Saturday and there will need to be many more cars on the road than last week. In order to get drivers to go online, we're assessing the following two bonus options in terms of cost:
# 
# Option 1: $50 for each driver that is online at least 8 hours, accepts 90% of requests, completes 10 trips, and has a rating of 4.7 or better during the time frame;
# Option 2: $4/trip for all drivers who complete 12 trips, and have a 4.7 or better rating.
# Using the dataset provided and given Scenario 1, provide answers to the questions below:
# 
# How much would the total bonus payout be with Option 1?
# How much would the total bonus payout be with Option 2?
# How many drivers would qualify for a bonus under Option 1 but not under Option 2?
# What percentages of drivers online completed less than 10 trips, had an acceptance rate of less than 90%, and had a rating of 4.7 or higher?
# Scenario 2: A taxi driver currently generates $200 per day in fares (before expenses), works six days a week, takes three weeks off, and has the following expenses:
# 
# Gas - $200 per week
# Insurance - $400 per month
# Vehicle rent (by the week) - $500
# The driver doesn't pay gas and rent expenses on off weeks.
# 
# Now, let's assume that the same driver would buy a Town Car and partner with Uber. If he does, his gas expenses would go up by 5%, his insurance expense would decrease by 20%, and he would no longer be renting a vehicle. However, he would need to buy a car. The driver would still take three weeks off per year.
# 
# Given Scenario 2, provide answers to the questions below:
# 
# How much money (after expenses) does the taxi driver make per year without partnering with Uber?
# You are convincing the same driver above to buy a Town Car and partner with Uber. Assuming the new car is 40.000 USD, how much would the driver's gross fares need to increase per week to fully pay for the car in year 1 and maintain the same yearly profit margin as before?

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('dataset_2.csv')
df.head(10)


# In[3]:


df.info()


# In[4]:


df.isna().sum()


# Question 1
# It is going to be a huge Saturday and there will need to be many more cars on the road than last week. In order to get drivers to go online, we're assessing the following two bonus options in terms of cost:
# 
# Option 1: $50 for each driver that is online at least 8 hours, accepts 90\% of requests, completes 10 trips, and has a rating of 4.7 or better during the time frame.
# 
# Option 2: $4 trip for all drivers who complete 12 trips, and have a 4.7 or better rating.
# 
# How much would the total bonus payout be with Option 1?

# In[5]:


df['Accept Rate'] = df['Accept Rate'].apply(lambda x: float(x[:-1]))


# In[6]:


df


# In[22]:


fo = df[(df['Supply Hours'] >= 8) & (df['Trips Completed'] >= 10) & (df['Accept Rate'] >= 90) & (df['Rating'] >= 4.7)]


# In[23]:


total_fo = 50 * f.shape[0]


# In[25]:


str(total_fo) + '$'


# Question 2
# 
# How much would the total bonus payout be with option 2?

# In[26]:


so = df[(df['Trips Completed'] >= 12) & (df['Rating'] >= 4.7)]
so


# In[27]:


total_so = 4 * so['Trips Completed'].sum()


# In[28]:


str(total_so) + '$'


# Question 3
# 
# How many drivers would qualify under Option 1 but not under Option 2?

# In[36]:


df_all = fo.merge(so, on='Name', how='left')


# In[37]:


df_all


# In[39]:


df_all[df_all['Rating_y'].isnull()]


# Question 4
# 
# What percentages of drivers online completed less than 10 trips, had an acceptance rate of less than 90%, and had a rating of 4.7 or higher?

# In[40]:


less = df[(df['Trips Completed'] < 10) & (df['Accept Rate'] < 90) & (df['Rating'] >= 4.7)]
less


# In[43]:


less.shape[0] / df.shape[0] * 100


# Question 5
# A taxi driver currently generates $200 per day in fares (before expenses), works six days a week, takes three weeks off, and has the following expenses:
# 
# Gas: 200 USD per week
# Insurance: 400 USD per month
# Vehicle rent (by the week): 500 USD
# The driver doesn't pay gas and rent expenses on off weeks.
# 
# How much money (after expenses) does the driver make per year?

# In[76]:


total_weeks_per_year = 52
weeks_off = 3
fare_per_day = 200 
workday_per_week = 6
total_months_per_year = 12
gas_per_week = 200
insurance_per_month = 400
vehicle_rent_by_week = 500


# In[77]:


total_expenses = (gas_per_week + vehicle_rent_by_week) * (total_weeks_per_year - weeks_off) + insurance_per_month * total_months_per_year


# In[78]:


str(total_expenses) + '$'


# In[79]:


total_revenue = (total_weeks_per_year - weeks_off) * workday_per_week * fare_per_day


# In[80]:


str(total_revenue) + '$'


# In[81]:


profit_margin = total_revenue - total_expenses


# In[82]:


str(profit_margin) + '$'


# Question 6
# 
# You are convincing the same driver above to buy a Town Car and partner with Uber.
# 
# If he does, his gas expenses would go up by 5%, his insurance expense would decrease by 20%, and he would no longer be renting a vehicle. However, he would need to buy a car. The driver would still take three weeks off per year.
# 
# Assuming the new car is 40.000 USD, how much would the driver's gross fares need to increase per week to fully pay for the car in year 1 and maintain the same yearly profit margin as before?

# In[83]:


gas_per_week = gas_per_week * 1.05
insurance_per_month = insurance_per_month * 0.8
new_car = 40000

new_total_expenses = new_car + gas_per_week * (total_weeks_per_year - weeks_off) + insurance_per_month * total_months_per_year


# In[84]:


str(new_total_expenses) + '$'


# In[85]:


new_profit_margin = total_revenue - new_total_expenses


# In[86]:


str(new_profit_margin) + '$'


# In[88]:


fare_increase = (profit_margin - new_profit_margin) / (total_weeks_per_year - weeks_off)


# In[89]:


str(fare_increase) + '$'

