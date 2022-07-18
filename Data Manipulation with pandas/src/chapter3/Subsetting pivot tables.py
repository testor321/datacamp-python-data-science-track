import pandas as pd

temperatures = pd.read_csv("../../Datasets/temperatures.csv")

# Pivot temperature by city and year
# Add a year column to temperatures
temperatures['date'] = pd.to_datetime(temperatures['date'], errors='coerce')
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index=["country", "city"], columns="year")

# Subset for Egypt to India
print("Subset for Egypt to India")
print(temp_by_country_city_vs_year.loc["Egypt":"India"])

# Subset for Egypt, Cairo to India, Delhi
print("Subset for Egypt to India")
print(temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi")])

# Subset in both directions at once
print("Subset for Egypt to India")
print(temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi"), "2005":"2010"])
