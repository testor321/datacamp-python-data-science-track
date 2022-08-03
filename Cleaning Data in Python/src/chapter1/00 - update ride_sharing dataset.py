import pandas as pd
import numpy as np


# CREATING A RANDOM DATE COLUMN, AS NONE WAS PROVIDED IN CSV -DTS
def random_dates(dt_start, dt_end, n=10):
    start_u = dt_start.value // 10 ** 9
    end_u = dt_end.value // 10 ** 9

    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')


ride_sharing = pd.read_csv("../../Datasets/ride_sharing_new.csv")

# added columns
# tire_sizes : int
# duration_trim : int
# ride_date : date
# ride_id : int


# updated columns
# user_type_cat : category

#
# Create a tire_size with random selection of 26, 27, and 29 as the options
ride_sharing['tire_sizes'] = np.random.choice([26,27,29], ride_sharing.shape[0])

#
# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')

# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype == 'category'

#
# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

#
# Setting range for random dates
start = pd.to_datetime('2015-01-01')
end = pd.to_datetime('2023-01-01')

# VALUES ARE INTENTIONALLY BEYOND THE CURRENT DATE - DTS
ride_sharing['ride_date'] = random_dates(start, end, n=25760)

# What you want is a datetime.date object. What you have been a datetime.datetime object
ride_sharing['ride_date'] = pd.to_datetime(ride_sharing['ride_date']).dt.date


#
# Create a ride_id with random selection from a range
ride_sharing['ride_id'] = np.random.choice(np.arange(start=0, stop=500000), ride_sharing.shape[0])

ride_sharing.to_csv("../../Datasets/ride_sharing_v1.csv")