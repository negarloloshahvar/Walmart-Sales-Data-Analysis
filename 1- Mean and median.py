import pandas as pd
sales_csv = pd.read_csv('sales_subset.csv', index_col= 0)
sales = pd.DataFrame(sales_csv)

print(sales)

# Explore your new DataFrame first by printing the first few rows of the sales DataFrame.
print(sales.head())
# Print information about the columns in sales.
print(sales.info())
# Print the mean of the weekly_sales column.
print(sales['weekly_sales'].mean())
# Print the median of the weekly_sales column.
print(sales['weekly_sales'].median())