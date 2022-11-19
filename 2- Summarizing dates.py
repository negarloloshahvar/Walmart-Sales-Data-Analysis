import pandas as pd
sales_csv = pd.read_csv('sales_subset.csv', index_col= 0)
sales = pd.DataFrame(sales_csv)

print(sales['date'].max())
print(sales['date'].min())