import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

sns.set_theme(style='darkgrid')

sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='whitegrid')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='white')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})

sns.lineplot(x='x', y='y', data=data)
plt.show()

df = pd.read_csv('AI_Usage_and_Impact_on_Students_and_Professionals.csv', delimiter=",", index_col='User_ID')

print(df.dtypes)
dffilter = df.head(40)
dffilter100 = df.head(100)

sns.set(style="whitegrid")

g = sns.displot(data=dffilter, x="AI_Tool", y="Productivity_Score", hue="User_Type", kind='hist')
g.figure.suptitle("sns.displot(data=dffilter, x=AI_Tool, y=Productivity_Score, hue=User_Type, kind='hist')")
g.figure.show()
read = input("Wait for me....")

g = sns.displot(data=dffilter, x="Productivity_Score", y="Satisfaction_Score", kind='kde')
g.figure.suptitle("sns.displot(data=dffilter, x=Productivity_Score, y=Satisfaction_Score, kind='kde')")
g.figure.show()
read = input("Wait for me....")

g = sns.kdeplot(data=dffilter, x="Productivity_Score")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=Productivity_Score)")
g.figure.show()
read = input("Wait for me....")

g = sns.histplot(data=dffilter, x='AI_Tool', y='Productivity_Score', hue='AI_Tool', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='AI_Tool', y='Productivity_Score', hue='AI_Tool', multiple=stack)")
g.figure.show()
read = input("Wait for me....")

g = sns.scatterplot(x='AI_Tool', y='Productivity_Score', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='AI_Tool', y='Productivity_Score', data=dffilter)")
g.figure.show()
read = input("Wait for me....")

g = sns.lineplot(data=dffilter, x="AI_Tool", y="Productivity_Score")
g.figure.suptitle("sns.lineplot(data=dffilter, x=AI_Tool, y=Productivity_Score)")
g.figure.show()
read = input("Wait for me....")

g = sns.barplot(data=dffilter, x="AI_Tool", y="Productivity_Score", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=AI_Tool, y=Productivity_Score, legend=False)")
g.figure.show()
read = input("Wait for me....")

g = sns.catplot(data=dffilter, x="AI_Tool", y="Productivity_Score")
g.figure.suptitle("sns.catplot(data=df, x=AI_Tool, y=Productivity_Score)")
g.figure.show()
read = input("Wait for me....")

glue = dffilter.pivot(columns="AI_Tool", values="Productivity_Score")

g = sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=AI_Tool, values=Productivity_Score)")
g.figure.show()
read = input("Wait for me....")