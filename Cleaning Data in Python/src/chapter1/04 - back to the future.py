import datetime as dt
import pandas as pd
import numpy as np


# # CREATING A RANDOM DATE COLUMN, AS NONE WAS PROVIDED IN CSV -DTS
# def random_dates(start, end, n=10):
#     start_u = start.value // 10 ** 9
#     end_u = end.value // 10 ** 9
#
#     return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')


ride_sharing = pd.read_csv("../../Datasets/ride_sharing_v1.csv")

# Setting range for random dates
# start = pd.to_datetime('2015-01-01')
# end = pd.to_datetime('2023-01-01')

# VALUES ARE INTENTIONALLY BEYOND THE CURRENT DATE - DTS
# ride_sharing['ride_date'] = random_dates(start, end, n=25760)

# What you want is a datetime.date object. What you have been a datetime.datetime object
# ride_sharing['ride_date'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Create a tire_size with random selection of 26, 27, and 29 as the options
# ride_sharing['tire_sizes'] = np.random.choice([26, 27, 29], ride_sharing.shape[0])

# check data types
ride_sharing['ride_date'].dtypes

# Convert ride_date to datetime
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Save today's date
today = dt.date.today()
# today = pd.to_datetime('today').normalize()


# Set all in the future to today's date
# .loc takes all rows with that condition and that name, and turns it into whatever ''='' says
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today


# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())
