import pandas as pd 

# Creating a Series
data = [10, 20, 30, 40] 
series = pd.Series(data) 
print(series)

# Custom Index
series_with_index = pd.Series(data, index=['a', 'b', 'c', 'd']) 
print(series_with_index)

#Accessing by Index 
value = series_with_index['b'] 
print(value) 

#Accessing by Position 
value = series_with_index[1] 
print(value) 

#Basic Series Functions
print(series.sum())    
print(series.mean())   
print(series.max())   
print(series.min())  