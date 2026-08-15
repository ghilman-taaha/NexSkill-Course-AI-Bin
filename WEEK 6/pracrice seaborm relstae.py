import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv( r'E:\neskill\nexskill course ai bin\RealEstate-USA.csv',delimiter
=",")
g=sns.displot(data=df, x="status" , y="price" , hue="state",  kind='hist'  )
g.figure.suptitle("sns.displot(data=df, x=status , y=price , hue=state,  kind='hist'  )"  )

# Display the plot
plt . show()


df = pd.read_csv( r'E:\neskill\nexskill course ai bin\RealEstate-USA.csv',delimiter=",")
g = sns.lmplot( data=df, x="bed", y="price", col="state", hue="state", 
col_wrap=2, palette="muted",
 ci=None, height=4, scatter_kws={"s": 50, "alpha": 1})
plt . show()



df = pd.read_csv( r'E:\neskill\nexskill course ai bin\RealEstate-USA.csv',delimiter=",")
g=sns.relplot( data=df, x="house_size", y="price", hue="bed",
 size="bath", col="status", kind="line", palette="muted",
 height=5, aspect=.75, facet_kws=dict(sharex=False),)
 
plt.show()

df = pd.read_csv( r'E:\neskill\nexskill course ai bin\RealEstate-USA.csv',delimiter=",")
g=sns.violinplot(data=df, x="city", y="price", hue="bed",
               split=True, inner="quart", fill=False,palette="muted")
plt.show()

df = pd.read_csv( r'E:\neskill\nexskill course ai bin\RealEstate-USA.csv',delimiter=",")
bed_ranking = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 12.0]
g=sns.boxenplot(data=df, x="bed", y="price",
    color="b", order=bed_ranking, width_method="linear",)
plt.show()