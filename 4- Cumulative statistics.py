import pandas as pd
sales_csv = pd.read_csv('sales_subset.csv', index_col= 0)
sales = pd.DataFrame(sales_csv)

# Here we calculate the cumulative sum and cumulative max of a department's weekly sales, which will allow us to identify
# what the total sales were so far as well as what the highest weekly sales were so far.

# sales_1_1 contains the sales data for department 1 of store 1.
sales_1 = sales[sales['store'] == 1]
sales_1_1 = sales_1[sales_1['department'] == 1]

sales_1_1 = sales_1_1.sort_values('date', ascending= True)

sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()
sales_1_1['cum_max_weekly_sales'] = sales_1_1['weekly_sales'].cummax()

print(sales_1_1[['date', 'cum_weekly_sales', 'cum_max_weekly_sales']])