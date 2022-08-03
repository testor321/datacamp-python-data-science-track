import pandas as pd

banking = pd.read_csv('../../Datasets/banking.csv', index_col=0)

# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'

# Convert acct_amount where it is in euro to dollars
banking.loc[banking['acct_cur'] == 'euro', 'acct_amount'] = \
    banking.loc[banking['acct_cur'] == 'euro', 'acct_amount'] * 1.1

# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[banking['acct_cur'] == 'euro', 'acct_cur'] = 'dollar'

# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar'

print(banking.info())
