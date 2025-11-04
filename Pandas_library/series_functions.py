import pandas as pd

# what is series in pandas?
#  It is like a column in a table. A series is a 1-D array holding data of any type.

a = [1,2,3,4,5,6,]
data = pd.Series(a)
print(data)

# if nothing else if specified their index is label.

print(a[0], a[1])

# How to create a label?
b = [10,20, 40]
d1 = pd.Series(b, index = ['A','B','C'])
print(d1)
print(d1['C'])

#  if we use key/value pair as datatype(dictonary)
# then key becomes the label of the series

day = {'A': "Sunday", 'B':"Monday", 3:"Tuesday", 4:"Wednesday"}
print(pd.Series(day))
print(pd.Series(day['B']))