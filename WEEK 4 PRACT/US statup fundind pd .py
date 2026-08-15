#startup_growth_investment_data.csv
import pandas as pd


#  Read csv file to DataFrame
df = pd.read_csv(r'E:\neskill\nexskill course ai bin\startup_growth_investment_data.csv',delimiter=",")

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

# access the Industry column (agency equivalent)
agency = df['Industry']
print("access the Industry column: df : ")
print(agency)
print()

# access multiple columns (agency, agent equivalent)
agency_agent = df[['Industry', 'Country']]
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
second_row4 = df.loc[df['Industry'] == 'SaaS']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

# Selecting a single column using .loc
second_row5 = df.loc[:1, 'Industry']
print("#Selecting a single column using .loc")
print(second_row5)
print()

# Selecting multiple columns using .loc
second_row6 = df.loc[:, ['Industry', 'Country']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

# Selecting a slice of columns using .loc
second_row7 = df.loc[:1, 'Industry':'Investment Amount (USD)']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

# Combined row and column selection using .loc
second_row8 = df.loc[df['Industry'] == 'SaaS', 'Industry':'Investment Amount (USD)']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 1 : using .loc - default case - ends here


print("# Case 2 : using .loc with index_col - starts here")
df_index_col = pd.read_csv(r'E:\neskill\nexskill course ai bin\startup_growth_investment_data.csv', index_col='Startup Name')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

# Selecting a single row using .loc
second_row = df_index_col.loc['Startup_5']
print("#Selecting a single row using .loc")
print(second_row)
print()

# Selecting multiple rows using .loc
second_row2 = df_index_col.loc[['Startup_5', 'Startup_10']]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

# Selecting a slice of rows using .loc (sort_index first so label-slicing works cleanly)
df_index_col_sorted = df_index_col.sort_index()
second_row3 = df_index_col_sorted.loc['Startup_1':'Startup_100']
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

# Conditional selection of rows using .loc
second_row4 = df_index_col.loc[df_index_col['Industry'] == 'SaaS']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

# Selecting a single column using .loc
second_row5 = df_index_col.loc[:, 'Industry']
print("#Selecting a single column using .loc")
print(second_row5)
print()

# Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:, ['Industry', 'Country']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

# Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:, 'Industry':'Investment Amount (USD)']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

# Combined row and column selection using .loc
second_row8 = df_index_col.loc[df_index_col['Industry'] == 'SaaS', 'Industry':'Investment Amount (USD)']
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

# ============================================================
# DataFrame Manipulation
# ============================================================

# Add a New Row to a Pandas DataFrame
# columns order: Startup Name,Industry,Funding Rounds,Investment Amount (USD),Valuation (USD),Number of Investors,Country,Year Founded,Growth Rate (%)
df.loc[len(df.index)] = [
    "Startup_5001", "AI", 6, 999999999.99, 4999999999.99, 25, "Pakistan", 2023, 55.5
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

# delete Funding Rounds column (page_url equivalent)
df.drop('Funding Rounds', axis=1, inplace=True)
# delete Valuation (USD) column (property_type equivalent)
df.drop(columns='Valuation (USD)', inplace=True)
# delete Number of Investors column (location equivalent)
df.drop(['Number of Investors'], axis=1, inplace=True)
print("Modified DataFrame -  delete Funding Rounds, Valuation (USD), Number of Investors column :")
print(df)

# Rename Labels in a DataFrame
# rename column 'Year Founded' to 'Year Founded_Changed' (province_name equivalent)
df.rename(columns={'Year Founded': 'Year Founded_Changed'}, inplace=True)
# rename column 'Growth Rate (%)' (bedrooms equivalent)
df.rename(mapper={'Growth Rate (%)': 'Growth Rate (%)_Changed'}, axis=1, inplace=True)
print("Modified DataFrame  - Rename Labels :")
print(df)

# Example: Rename Row Labels
df.rename(index={0: 7}, inplace=True)
df.rename(mapper={4: 10, 6: 100}, axis=0, inplace=True)
print("Modified DataFrame - Rename Row Labels:")
print(df)

# query() to Select Data
selected_rows = df.query('Industry == "SaaS" or `Investment Amount (USD)` > 400000000')
print(selected_rows.to_string())
print(len(selected_rows))

# sort DataFrame by Investment Amount (USD) in ascending order (price equivalent)
sorted_df = df.sort_values(by='Investment Amount (USD)')
print(sorted_df.to_string(index=False))

# Sort by 'Investment Amount (USD)' and then by 'Country'
df1 = df.sort_values(by=['Investment Amount (USD)', 'Country'])
print("Sorting by 'Investment Amount (USD)' (ascending) and then by 'Country' (ascending):\n")
print(df1.to_string(index=False))

# Pandas groupby
grouped = df.groupby('Country')['Investment Amount (USD)'].sum()
print(grouped.to_string())
print("grouped :", len(grouped))

# Pandas Data Cleaning
df_cleaned = df.dropna()
print("Cleaned Data:\n", df_cleaned)

# filling NaN values with 0
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