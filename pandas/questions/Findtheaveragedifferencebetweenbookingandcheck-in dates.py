https://platform.stratascratch.com/coding/9614-find-the-average-difference-between-booking-and-check-in-dates/solutions?code_type=2

# Import your libraries
import pandas as pd

# Start writing coded
df = airbnb_contacts
df['ts_booking_at'] = pd.to_datetime(df.ts_booking_at).dt.date
df['ds_checkin'] = pd.to_datetime(df.ds_checkin).dt.date

df['diff'] =(df['ds_checkin'] - df['ts_booking_at'] ).dt.days
df = df.groupby('id_host')['diff'].mean().reset_index().dropna()
df[['id_host','diff']].sort_values(by='diff',ascending=False)
