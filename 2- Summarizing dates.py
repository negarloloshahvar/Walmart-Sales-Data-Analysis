import pandas as pd
import numpy as np
sales_csv = pd.read_csv('sales_subset.csv', index_col= 0)
sales = pd.DataFrame(sales_csv)

print(sales['date'].max())
print(sales['date'].min())