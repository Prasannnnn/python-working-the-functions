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

import pandas as pd

print(pd.options.display.max_rows)