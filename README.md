# Walmart-Sales-Data-Analysis

In this project I will analyze the Walmart Stores Sales dataset. Walmart Stores are a chains of department stores in the US. This Dataset contains information about Walmart store departments which includes ID number for each store, store type, amount of weekly sales (in USD), whether it was a holiday week, the average tempreture during the week (in Centigrade), average fuel price in each week per liter(in USD), and the national unemployment rate that week.

## Aggregating DataFrames

### Summary Statistics

- Summary Statistics summarize many numbers in one statistic. e.g. mean, median, minimum, maximum, and standard deviation. Calculating summary statistics allows you to get a better sense of your data, even if there's a lot of it. 
- By taking a closer look at the summary statistics of the walmart dataset we obtain that the mean weekly sales amount is almost double the median weekly sales amount! This can tell us that there are a few very high sales weeks that are making the mean so much higher than the median.
- Summary statistics can also be calculated on date columns that have values with the data type ```datetime64```. Taking the minimum and maximum of a column of dates is handy for figuring out what time period your data covers.


### The ```agg()``` Function
- The ```.agg()``` method allows us to apply our own custom functions to a DataFrame, as well as apply functions to more than one column of a DataFrame at once, making the aggregations super-efficient.
- The ```.agg()``` method makes it easy to compute multiple statistics on multiple columns, all in just one line of code.

### Cumulative statistics
- Cumulative statistics can also be helpful in tracking summary statistics over time.
  - ```cumsum()```
  - ```cummax()```
  - ```cummin()```

### Dropping duplicates
- Removing duplicates is an essential skill to get accurate counts because often, you don't want to count the same thing multiple times.
- We can remove duplicates by using the following method: ```df.drop_duplicates(subset='column name')```
- We also can pass a list to the subset argument.

### Counting categorical variables
- Counting is a great way to get an overview of the data and to spot curiosities that we might not notice otherwise.
- We do this with the help of ```.value_counts('column name')``` method.
- We can also use ```.value_counts('column name', sort= True)``` to sort the resulting column.
- We can also use ```.value_counts('column name', normalize= True)``` to view the proportion of each cell.

### Grouped Summary Statistics
- we can use ```.groupby()``` to calculate Summary Statistics just for specific groups.
