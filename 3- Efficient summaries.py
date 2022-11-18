import pandas as pd
import numpy as np
sales_csv = pd.read_csv('sales_subset.csv', index_col= 0)
sales = pd.DataFrame(sales_csv)

# Here "IQR" is short for inter-quartile range, which is the 75th percentile minus the 25th percentile.
# It's an alternative to standard deviation that is helpful if the data contains outliers.

def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

print(sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg([iqr, np.median]))


