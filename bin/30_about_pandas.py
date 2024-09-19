"""
Pandas library
- Pandas library has many classes and many functions
    which we can use it
- Few class names 'DataFrame', 'Series' etc
- Few function names: read_csv, read_excel etc

Main class in pandas library is : 'DataFrame'
- 'DataFrame' is developed for tabular data processing
    like csv, xlsx, db data
"""

print("Inside pandas library")
print("-"*20)
# --------------

import pandas as pd
print(dir(pd))

print("#"*40, end="\n\n")
################################

print("Inside DataFrame class")
print("-"*20)
# --------------

import pandas as pd
print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
################################

print("DataFrame example-1")
print("-"*20)
# --------------


my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80]])
print(my_df)

print("#"*40, end="\n\n")
################################

print("DataFrame example-2")
print("-"*20)
# --------------


my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80]], index=["r1", "r2"], columns=["c1", "c2", "c3", "c4"])
print(my_df)

print("#"*40, end="\n\n")
################################

print("min value in entire data")
print("-"*20)
# --------------


my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80]], index=["r1", "r2"], columns=["c1", "c2", "c3", "c4"])
print(my_df.min())

print("#"*40, end="\n\n")
################################

print("one minimum value in entire data")
print("-"*20)
# --------------


my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80]], index=["r1", "r2"], columns=["c1", "c2", "c3", "c4"])
print(my_df.min().min())

print("#"*40, end="\n\n")
################################


print("1st row average")
print("-"*20)
# --------------


my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80]], index=["r1", "r2"], columns=["c1", "c2", "c3", "c4"])
print(my_df.iloc[0,:]) # 0th row, : = all columns
print(my_df.iloc[0,:].mean())

print("#"*40, end="\n\n")
################################
