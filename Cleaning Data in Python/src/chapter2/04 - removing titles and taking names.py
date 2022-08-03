import pandas as pd

airlines = pd.read_csv("../../Datasets/airlines_final_v1.csv")

# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.", "", regex=True)

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.", "", regex=True)

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines["full_name"].str.replace("Miss", "", regex=True)

# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace('Ms.', "", regex=True)

# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False
