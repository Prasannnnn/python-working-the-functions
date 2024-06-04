# import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)

###############pandas series########
# import pandas as pd

# a = [1,7,2]

# b = pd.Series(a, index=["x","y","z"])

# print(b)
#############pandas Dataframe########
# import pandas as pd

# a = {
#     "calories":[420,300,400],
#     "duration":[50,40,45]
# }

# b=pd.DataFrame(a)
# print(b)

'''
Locate Row
As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)
'''

# print(b.loc[0])

# print(b.loc[[0,1]])

'''
Named Indexes:
With the index argument, you can name your own indexes.
'''
# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(df) 


'''
Read CSV Files:
A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

In our examples we will be using a CSV file called 'data.csv'.

'''
# import pandas as pd

# df = pd.read_csv('data.csv')

# print(df.to_string()) 

#use to_string() to print the entire DataFrame.

'''
If you have a large DataFrame with many rows, 
Pandas will only return the first 5 rows, and the last 5 rows:
'''

# import pandas as pd

# df = pd.read_csv('data.csv')

# print(df) 


'''
max_rows:
The number of rows returned is defined in Pandas option settings.

You can check your system's maximum rows with the pd.options.display.max_rows statement.
'''

# import pandas as pd

# print(pd.options.display.max_rows)


'''
Pandas - Analyzing Dataframes
Viewing the Data:
One of the most used method for getting a quick overview of the DataFrame, is the head() method.

The head() method returns the headers and a specified number of rows, starting from the top.
'''

# import pandas as pd

# df = pd.read_csv('data.csv')

# print(df.head(10))

#print the first five rows:
import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())


'''
There is also a tail() method for viewing the last rows of the DataFrame.

The tail() method returns the headers and a specified number of rows, starting from the bottom.
'''

print(df.tail())


'''
Info About the Data
The DataFrames object has a method called info(), that gives you more information about the data set.
'''


print(df.info())

'''
Result Explained
The result tells us there are 169 rows and 4 columns:


  RangeIndex: 169 entries, 0 to 168
  Data columns (total 4 columns):

And the name of each column, with the data type:


   #   Column    Non-Null Count  Dtype  
  ---  ------    --------------  -----  
   0   Duration  169 non-null    int64  
   1   Pulse     169 non-null    int64  
   2   Maxpulse  169 non-null    int64  
   3   Calories  164 non-null    float64

Null Values
The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. 

'''