import pandas as pd

df =pd.read_csv(r'E:\neskill\NexSkill course AI bin\RealEstate-USA.csv',delimiter=",")
print (df)

print("df - data type", df.dtypes)
print("df.info():",df.info())

print('Last three Rows:')
print(df.tail(3))

print('First three Rows:')
print(df.head(3))
print()

print("Summary of Statistics of DataFrame using describe() method", df.describe())

print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()

status = df["status"]
print("access the Name column: df : ")
print(status)
print()

status_price = df[['status','price']]
print("access multiple columns: df : ")
print(status_price)
print()

second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df.loc[[2, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

second_row3 = df.loc[2:8]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

second_row4 = df.loc[df['status'] == 'Gateway Properties']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

second_row5 = df.loc[:1,'status']
print("#Selecting a single column using .loc")
print(second_row5)
print()

second_row6 = df.loc[:,['status','price']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

second_row7 = df.loc[:1,'brokered_by':'status']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

second_row8 = df.loc[df['status'] == 'Gateway Properties','price':'status']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

#USING .iloc
print("#Selecting a single row using .iloc")
print(second_row)
print()

rows = df.iloc[1:5,1]
print(rows)
print()

