import pandas as pd

df = pd.read_csv(r'E:\neskill\NexSkill course AI bin\OR_hos_prices1.csv',delimiter=",")

df.rename(columns={'Unnamed: 0': 'hospital'}, inplace=True)

print(df)

print("df - data types" , df.dtypes)

print("df.info():   " , df.info() )

print('Last three Rows:')
print(df.tail(3))

print('First Three Rows:')
print(df.head(3))
print()

print("Summary of Statistics of DataFrame using describe() method", df.describe())

print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()


hospital_col = df['hospital']
print("access the hospital column: df : ")
print(hospital_col)
print()

hospital_address = df[['hospital','address']]
print("access multiple columns: df : ")
print(hospital_address)
print()


second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

second_row4 = df.loc[df['hospital'] == 'Providence St Vincent Medical Center']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

second_row5 = df.loc[:1,'hospital']
print("#Selecting a single column using .loc")
print(second_row5)
print()

second_row6 = df.loc[:,['hospital','address']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

second_row7 = df.loc[:1,'address':'long']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

second_row8 = df.loc[df['hospital'] == 'Providence St Vincent Medical Center','address':'long']
print("#Combined row and column selection using .loc")
print(second_row8)
print()


print("# Case 2 : using .loc with index_col - starts here")
df_index_col = pd.read_csv('OR_hos_prices1.csv', index_col=0)
df_index_col.index.name = 'hospital'

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

second_row = df_index_col.loc['Providence St Vincent Medical Center']
print("#Selecting a single row using .loc")
print(second_row)
print()

second_row2 = df_index_col.loc[['Providence St Vincent Medical Center', 'Asante Ashland Community Hospital']]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

second_row3 = df_index_col.loc['Mid-Columbia Medical Center':'Providence St Vincent Medical Center']
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

second_row4 = df_index_col.loc[df_index_col['Hip Replacement'] > 30000]
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

second_row5 = df_index_col.loc[:,'address']
print("#Selecting a single column using .loc")
print(second_row5)
print()

second_row6 = df_index_col.loc[:,['address','lat']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

second_row7 = df_index_col.loc[:,'address':'long']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

second_row8 = df_index_col.loc[df_index_col['Hip Replacement'] > 30000,'address':'long']
print("#Combined row and column selection using .loc")
print(second_row8)
print()



print("# Case 3 : Using .iloc - starts here")
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

second_row2 = df_index_col.iloc[[1, 3, 5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

second_row5 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

second_row6 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

second_row7 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

second_row8 = df_index_col.iloc[[1, 3, 5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()


print("Next Run")

new_row = pd.Series([None] * len(df.columns), index=df.columns)
new_row['hospital'] = 'Test Hospital'
new_row['address'] = '123 Test St, Test City, OR 00000, USA'
new_row['lat'] = 45.0
new_row['long'] = -122.0
new_row['Hip Replacement'] = 30000

df.loc[len(df.index)] = new_row
print("Modified DataFrame - add a new row:")
print(df)
print()



df.drop(1, axis=0, inplace=True)
df.drop(index=2, inplace=True)
df.drop([3, 5], axis=0, inplace=True)
print("Modified DataFrame - Remove Rows:")
print(df)


df.drop('Tonsillectomy', axis=1, inplace=True)
df.drop(columns='Breast Biopsy', inplace=True)
df.drop(['CVC Insertion', 'Hysteroscopy'], axis=1, inplace=True)
print("Modified DataFrame -  delete Tonsillectomy, Breast Biopsy, CVC Insertion, Hysteroscopy columns:")
print(df)


df.rename(columns={'address': 'address_Changed'}, inplace=True)
df.rename(mapper={'lat': 'lat_Changed', 'long': 'long_Changed'}, axis=1, inplace=True)
print("Modified DataFrame  - Rename Labels :")
print(df)


df.rename(index={0: 7}, inplace=True)
df.rename(mapper={4: 10, 6: 100}, axis=0, inplace=True)
print("Modified DataFrame - Rename Row - 0 >>> 7 , 4 >>> 10 , 6 >>> 100 Labels:")
print(df)



selected_rows = df.query('hospital == "Providence St Vincent Medical Center" or `Hip Replacement` > 30000')

print(selected_rows.to_string())
print(len(selected_rows))


sorted_df = df.sort_values(by='Hip Replacement')
print(sorted_df.to_string(index=False))


df1 = df.sort_values(by=['Hip Replacement', 'lat_Changed'])

print("Sorting by 'Hip Replacement' (ascending) and then by 'lat_Changed' (ascending):\n")
print(df1.to_string(index=False))



grouped = df.groupby('lat_Changed')['Hip Replacement'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))


df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)


df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)


data = [2, 4, 6, 8]
array1 = pd.array(data)
print(array1)

int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()