
import pandas as pd

df = pd.read_csv( r'E:\neskill\NexSkill course AI bin\FINAL-ASSESSMENT\10-diamonds.csv')

print(df)

print("df - data types", df.dtypes)

print("df.info():   ", df.info())

# display the last three rows
print('Last three Rows:')
print(df.tail(3))

# display the first three rows
print('First Three Rows:')
print(df.head(3))
print()

# Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

# Counting the rows and columns in DataFrame using shape().
print("Counting the rows and columns in DataFrame using shape() : ", df.shape)
print()

# access the cut column
agency = df['cut']
print("access the cut column: df : ")
print(agency)
print()

# access multiple columns
agency_agent = df[['cut', 'color']]
print("access multiple columns: df : ")
print(agency_agent)
print()

# Case 1 : using .loc - default case - starts here
# Selecting a single row using .loc
second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

# Selecting multiple rows using .loc
second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

# Selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

# Conditional selection of rows using .loc
second_row4 = df.loc[df['cut'] == 'Fair']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

# Selecting a single column using .loc
second_row5 = df.loc[:1, 'cut']
print("#Selecting a single column using .loc")
print(second_row5)
print()

# Selecting multiple columns using .loc
second_row6 = df.loc[:, ['cut', 'color']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

# Selecting a slice of columns using .loc
second_row7 = df.loc[:1, 'cut':'price']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

# Combined row and column selection using .loc
second_row8 = df.loc[df['cut'] == 'Fair', 'cut':'price']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 1 : using .loc - default case - ends here


print("# Case 2 : using .loc with index_col - starts here")
df_index_col = pd.read_csv( r'E:\neskill\NexSkill course AI bin\FINAL-ASSESSMENT\10-diamonds.csv', index_col='Unnamed: 0')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

# Selecting a single row using .loc
second_row = df_index_col.loc[20001]
print("#Selecting a single row using .loc")
print(second_row)
print()

# Selecting multiple rows using .loc
second_row2 = df_index_col.loc[[20001, 20031]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

# Selecting a slice of rows using .loc (sort_index first so slicing works cleanly)
df_index_col_sorted = df_index_col.sort_index()
second_row3 = df_index_col_sorted.loc[20001:20097]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

# Conditional selection of rows using .loc
second_row4 = df_index_col.loc[df_index_col['cut'] == 'Fair']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

# Selecting a single column using .loc
second_row5 = df_index_col.loc[:, 'cut']
print("#Selecting a single column using .loc")
print(second_row5)
print()

# Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:, ['cut', 'color']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

# Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:, 'cut':'price']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

# Combined row and column selection using .loc
second_row8 = df_index_col.loc[df_index_col['cut'] == 'Fair', 'cut':'price']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 2 : using .loc with index_col  -  ends here


print("# Case 3 : Using .iloc - starts here")
# Selecting a single row using .iloc
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

# Selecting multiple rows using .iloc
second_row2 = df_index_col.iloc[[1, 3, 5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

# Selecting a slice of rows using .iloc
second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

# Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:, 2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

# Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:, [2, 4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

# Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:, 2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

# Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3, 5], 2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()
# Case 3 : Using .iloc - ends here

print("Next Run")


# Add a New Row to a Pandas DataFrame

df.loc[len(df.index)] = [
    9999999, 0.5, "Ideal", "E", "VS1", 61.5, 55.0, 5000, 5.1, 5.1, 3.1
]
print("Modified DataFrame - add a new row:")
print(df)
print()

# Remove Rows/Columns from a Pandas DataFrame

# delete row with index 1
df.drop(1, axis=0, inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
print("Modified DataFrame - Remove Rows:")
print(df)

# delete z column
df.drop('z', axis=1, inplace=True)
# delete y column
df.drop(columns='y', inplace=True)
# delete depth and table columns
df.drop(['depth', 'table'], axis=1, inplace=True)
print("Modified DataFrame -  delete z, y, depth, table column :")
print(df)

# Rename Labels in a DataFrame
# rename column 'carat' to 'carat_Changed'
df.rename(columns={'carat': 'carat_Changed'}, inplace=True)
# rename columns 'clarity' and 'x'
df.rename(mapper={'clarity': 'clarity_Changed', 'x': 'x_Changed'}, axis=1, inplace=True)
print("Modified DataFrame  - Rename Labels :")
print(df)

# Example: Rename Row Labels
df.rename(index={0: 7}, inplace=True)
df.rename(mapper={4: 10, 6: 100}, axis=0, inplace=True)
print("Modified DataFrame - Rename Row Labels:")
print(df)

# query() to Select Data
selected_rows = df.query('cut == "Fair" or price > 15000')
print(selected_rows.to_string())
print(len(selected_rows))

# sort DataFrame by price in ascending order
sorted_df = df.sort_values(by='price')
print(sorted_df.to_string(index=False))

# Sort by 'price' and then by 'cut'
df1 = df.sort_values(by=['price', 'cut'])
print("Sorting by 'price' (ascending) and then by 'cut' (ascending):\n")
print(df1.to_string(index=False))

# Pandas groupby
grouped = df.groupby('cut')['price'].sum()
print(grouped.to_string())
print("grouped :", len(grouped))

# Pandas Data Cleaning
df_cleaned = df.dropna()
print("Cleaned Data:\n", df_cleaned)


df = df.astype(object)
df.fillna(0, inplace=True)
print("\nData after filling NaN with 0:\n", df)

# create a list named data
data = [2, 4, 6, 8]
array1 = pd.array(data)
print(array1)

# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()

# to be continued....