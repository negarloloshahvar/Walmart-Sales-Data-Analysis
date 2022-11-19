import pandas as pd
sales_csv = pd.read_csv('sales_subset.csv', index_col= 0)
sales = pd.DataFrame(sales_csv)

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset= ['store', 'type'])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset= ['store', 'department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday'] == True].drop_duplicates(subset= 'date')

# Print date col of holiday_dates
print(holiday_dates[['date']])