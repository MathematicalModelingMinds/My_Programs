import pandas as pd
df = pd.read_csv("Sales.csv")
print(df)

# Viewing data
df.head() 

df.tail(3)

df['Country']

df['Total Profit'].min()

df['Total Profit'].max()

df['Total Profit'].mean()

df['Total Profit'].sum()

df.sum()

# Methods
df.columns
df.index
df.info()
df.describe()

# Slicing
print(df['Country'])
type(df['Country'])

print(df[['Country']])
type(df[['Country']])

print(df[['Country','Total Profit']])

# Slicing operations
df['Country'][3:20] 

df.loc[:,['Country']].head()
df.loc[:,'Country'].head()

# Filtering
df['Item Type'].unique()
df['Item Type'].nunique()
df['Item Type'].value_counts()

# Conditional filters
Set_of_boolean_values = df['Item Type']=='Baby Food'
print(Set_of_boolean_values)

Baby_food_sales = (df[Set_of_boolean_values])
print(Baby_food_sales)

# Compute the sum
import numpy as np
a = np.array(Baby_food_sales)
print(a)

b = a[:,5]
print(b)
sum = 0
for i in range(0,len(b)):    
    sum = sum + b[i]
print(sum)

# Combine filters
UnitsSold_filter = df['Units Sold']>=4000
df.loc[UnitsSold_filter,:]

Item_filter = df['Item Type']=='Baby Food'
df.loc[Item_filter,:]

df.loc[UnitsSold_filter & Item_filter, :]

# Missing data
df.info()

df['Total Profit'].isna()
Profit_missing = df['Total Profit'].isna()
df.loc[Profit_missing,:]

# Remove missing data
df.dropna(how = 'any')

# Filling missing values
df['Total Profit'][20:25].fillna(0) # Fill with the value of 0
df['Total Profit'][20:25].fillna(method='bfill') # Fill with the value of next index
df['Total Profit'][20:25].fillna(method='ffill') # Fill with the value of previous index
df['Total Profit'][20:25].interpolate(method='linear') # Fill with the value after linear interpolation

Profit_missing = df['Total Profit'].isna() # Fill with real value
df.loc[Profit_missing,'Total Profit'] = 339490.5-216804.0
df['Total Profit'][20:25]


# NumPy and Pandas
import numpy as np
import pandas as pd

arr = np.arange(0,21).reshape(7,3)
print(arr)

df = pd.DataFrame(data=arr)
print(df)
df = pd.DataFrame(data=arr,columns=['X','Y','Z'])
print(df)

# Managing columns
# Rename
df = df.rename(columns={'Item Type':'Item_Type',
                       'Units_Sold':'Units_Sold',
                       'Total Revenue':'Total_Revenue',
                       'Total Cost':'Total_Cost',
                       'Total Profit':'Total_Profit'})

df.columns = ['Country_Name', 'Item_Type', 'Units_Sold', 
             'Total_Revenue', 'Total_Cost', 'Total_Profit']

# Delete
df = df.drop(columns=['Total_Revenue'])  
del df['Total_Cost']      

# Export data frame
df.to_csv(path_or_buf='Python_Pandas\Sales.csv',index=False)
df.to_excel(excel_writer='Python_Pandas\Sales.xlsx',index=False