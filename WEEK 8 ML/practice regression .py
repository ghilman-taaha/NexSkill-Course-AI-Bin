import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'E:\neskill\NexSkill course AI bin\WEEK 8 ML\housing.csv')

print(df.head())

print("df.shape:         " , df.shape)

df.plot.scatter(x='longitude', y='latitude', title='Scatter Plot of hours and scores percentages');
plt.show()


print("df.describe():                    " , df.describe())


print(" df['longitude'] :     " , df['longitude'])
print("  df['latitude']   :    ", df['latitude']   )

y = df['longitude'].values.reshape(-1, 1)
X = df['latitude'].values.reshape(-1, 1)

print("y :  " , y)
print("X :   " , X)

print(df['latitude'].values) 
print(df['latitude'].values.shape)