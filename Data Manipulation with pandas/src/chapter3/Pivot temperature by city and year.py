import pandas as pd

temperatures = pd.read_csv("../../Datasets/temperatures.csv")

# Pivot temperature by city and year
# Add a year column to temperatures
temperatures['date'] = pd.to_datetime(temperatures['date'], errors='coerce')
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index=["country", "city"], columns="year")

# See the result
print(temp_by_country_city_vs_year)
