import pandas as pd

# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv("../../Datasets/airline_bumping.csv")

# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values("bumps_per_10k", ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv("../../Datasets/airline_totals_sorted.csv")
