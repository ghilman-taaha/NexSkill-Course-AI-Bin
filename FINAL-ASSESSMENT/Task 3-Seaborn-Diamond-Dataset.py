import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# Sample data
data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

# Set the theme
sns.set_theme(style='darkgrid')
# Create a plot
sns.lineplot(x='x', y='y', data=data)
plt.show()

# Other themes can be set similarly
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


# Customize the theme
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})

# Create a plot
sns.lineplot(x='x', y='y', data=data)
plt.show()


#Diamonds data - based examples
# Load data from a CSV file
df = pd.read_csv(r'E:\neskill\NexSkill course AI bin\FINAL-ASSESSMENT\10-diamonds.csv', index_col='Unnamed: 0')

print(df.dtypes)
dffilter= df
dffilter100= df.head(100)


sns.set(style="whitegrid")


#kind='hist'  
# Graph 1 - histogram of cut and price
g=sns.displot(data=dffilter, x="cut" , y="price" , hue="color",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=cut , y=price , hue=color,  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#kind='kde'
# Graph 2 - kde plot of price and carat
g=sns.displot(data=dffilter, x="price" , y="carat" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=price , y=carat , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#kind='kde'
# Graph 3 - kde plot of price
g=sns.kdeplot(data=dffilter, x="price")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=price)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
# Graph 4 - stacked histogram of price by cut
g = sns.histplot(data=dffilter, x='cut', y='price', hue='cut', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='cut', y='price', hue='cut', multiple=stack)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
# Graph 5 - scatter plot of cut and price
g = sns.scatterplot(x='cut', y='price', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='cut', y='price', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
# Graph 6 - line plot of cut and price
g=sns.lineplot(data=dffilter, x="cut" , y="price"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=cut , y=price  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
# Graph 7 - bar plot of price for each cut
g=sns.barplot(data=dffilter, x="cut", y="price", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=cut, y=price, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
# Graph 8 - cat plot of price for each cut
g=sns.catplot(data=dffilter, x="cut", y="price")
g.figure.suptitle("sns.catplot(data=df, x=cut, y=price)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
glue = dffilter.pivot(columns="cut", values="price")

# Graph 9 - heatmap of price for each cut
g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=cut, values=price)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")


sns.set_theme(style="ticks", palette="pastel")

# Graph 10 - boxplot of price by cut and color
g = sns.boxplot(x="cut", y="price",
            hue="color",
            data=df)
sns.despine(offset=10, trim=True)
g.figure.suptitle("sns.boxplot(x=cut, y=price, hue=color, data=df)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")


sns.set_theme(style="dark")

# Graph 11 - violin plot 
g = sns.violinplot(data=df[df["color"].isin(["D", "J"])], x="cut", y="price", hue="color",
               split=True, inner="quart", fill=False,
               palette={"D": "g", "J": ".35"})
g.figure.suptitle("sns.violinplot(x=cut, y=price, hue=color, split=True)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")


sns.set_theme(style="ticks")

x = df["carat"]
y = df["price"]

# Graph 12 - hex jointplot of carat and price
g = sns.jointplot(x=x, y=y, kind="hex", color="#4CB391")
g.figure.suptitle("sns.jointplot(x=carat, y=price, kind=hex)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")


sns.set_theme(style="ticks")

# Graph 13 - kde jointplot of carat and price
g = sns.jointplot(
    data=df,
    x="carat", y="price", hue="cut",
    kind="kde",
)
g.figure.suptitle("sns.jointplot(x=carat, y=price, hue=cut, kind=kde)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")


sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

# Initialize the FacetGrid object
pal = sns.cubehelix_palette(5, rot=-.25, light=.7)
g = sns.FacetGrid(df, row="cut", hue="cut", aspect=15, height=.5, palette=pal)

# Draw the densities in a few steps
g.map(sns.kdeplot, "price",
      bw_adjust=.5, clip_on=False,
      fill=True, alpha=1, linewidth=1.5)
g.map(sns.kdeplot, "price", clip_on=False, color="w", lw=2, bw_adjust=.5)

g.refline(y=0, linewidth=2, linestyle="-", color=None, clip_on=False)



def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)


g.map(label, "price")

# Set the subplots to overlap
g.figure.subplots_adjust(hspace=-.25)


g.set_titles("")
g.set(yticks=[], ylabel="")
g.despine(bottom=True, left=True)
# Graph 14 - ridgeline plot of price for each cut
g.figure.suptitle("sns.FacetGrid(df, row=cut, hue=cut) - kdeplot of price"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")


sns.set_theme(style="white")

d = df[["carat", "depth", "table", "price", "x", "y", "z"]]

corr = d.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Graph 15 - correlation heatmap
g = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
g.figure.suptitle("sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, center=0, square=True)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")