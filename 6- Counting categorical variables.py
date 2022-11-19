import pandas as pd
sales_csv = pd.read_csv('sales_subset.csv', index_col= 0)
sales = pd.DataFrame(sales_csv)

store_types = sales.drop_duplicates(subset= ['store', 'type'])
store_depts = sales.drop_duplicates(subset= ['store', 'department'])

