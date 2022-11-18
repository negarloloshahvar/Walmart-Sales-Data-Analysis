# Walmart-Sales-Data-Analysis

In this project I will analyze the Walmart Stores Sales dataset. Walmart Stores are a chains of department stores in the US. This Dataset contains information about Walmart store departments which includes ID number for each store, store type, amount of weekly sales (in USD), whether it was a holiday week, the average tempreture during the week (in Centigrade), average fuel price in each week per liter(in USD), and the national unemployment rate that week.

## Aggregating DataFrames

### Summary Statistics

- Summary Statistics summarize many numbers in one statistic. e.g. mean, median, minimum, maximum, and standard deviation. Calculating summary statistics allows you to get a better sense of your data, even if there's a lot of it. 
- By taking a closer look at the summary statistics of the walmart dataset we obtain that the mean weekly sales amount is almost double the median weekly sales amount! This can tell us that there are a few very high sales weeks that are making the mean so much higher than the median.
- Summary statistics can also be calculated on date columns that have values with the data type ```datetime64```. Taking the minimum and maximum of a column of dates is handy for figuring out what time period your data covers.


### The ```agg()``` Function
- The ```.agg()``` method allows you to apply your own custom functions to a DataFrame, as well as apply functions to more than one column of a DataFrame at once, making your aggregations super-efficient.
