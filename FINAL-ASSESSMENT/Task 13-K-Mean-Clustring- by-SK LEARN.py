import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# data, carat and price (scaled)
diamonds_data = pd.read_csv(r'E:\neskill\NexSkill course AI bin\FINAL-ASSESSMENT\10-diamonds.csv', index_col='Unnamed: 0')
X = StandardScaler().fit_transform(diamonds_data[['carat', 'price']].values)

plt.figure(figsize=(7.5, 3.5))
plt.scatter(X[:, 0], X[:, 1], s=20, cmap='summer');
plt.show()

kmeans = KMeans(n_clusters=3, max_iter=100)

kmeans.fit(X)


plt.figure(figsize=(7.5, 3.5))
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, s=20, cmap='summer')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
marker='x', c='r', s=50, alpha=0.9)
plt.show()


df = diamonds_data
dffilter= df

sns.set(style="whitegrid")


# Graph 1 - displot (hist): cut, price, color
g=sns.displot(data=dffilter, x="cut" , y="price" , hue="color",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=cut , y=price , hue=color,  kind='hist'  )"  )

plt.show()
# Graph 2 - displot (kde): price, carat
g=sns.displot(data=dffilter, x="price" , y="carat" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=price , y=carat , kind='kde'  )"  )

plt.show()
# Graph 3 - kdeplot: price
g=sns.kdeplot(data=dffilter, x="price")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=price)"  )

plt.show()
# Graph 4 - histplot: cut, price
g = sns.histplot(data=dffilter, x='cut', y='price', hue='cut', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='cut', y='price', hue='cut', multiple=stack)"  )
plt.show()
# Graph 5 - scatterplot: cut, price
g = sns.scatterplot(x='cut', y='price', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='cut', y='price', data=dffilter)"  )
plt.show()
# Graph 6 - lineplot: cut, price
g=sns.lineplot(data=dffilter, x="cut" , y="price"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=cut , y=price  )"  )
plt.show()
# Graph 7 - barplot: cut, price
g=sns.barplot(data=dffilter, x="cut", y="price", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=cut, y=price, legend=False)"  )
plt.show()
# Graph 8 - catplot: cut, price
g=sns.catplot(data=dffilter, x="cut", y="price")
g.figure.suptitle("sns.catplot(data=df, x=cut, y=price)"  )
plt.show() 
glue = dffilter.pivot(columns="cut", values="price")

# Graph 9 - heatmap: cut, price
g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=cut, values=price)"  )
plt.show()


sns.set_theme(style="ticks", palette="pastel")

# Graph 10 - boxplot: cut, price, color
g = sns.boxplot(x="cut", y="price",
            hue="color",
            data=df)
sns.despine(offset=10, trim=True)
g.figure.suptitle("sns.boxplot(x=cut, y=price, hue=color, data=df)"  )
plt.show()


sns.set_theme(style="dark")

# Graph 11 - violinplot: cut, price, color (D and J)
g = sns.violinplot(data=df[df["color"].isin(["D", "J"])], x="cut", y="price", hue="color",
               split=True, inner="quart", fill=False,
               palette={"D": "g", "J": ".35"})
g.figure.suptitle("sns.violinplot(x=cut, y=price, hue=color, split=True)"  )
plt.show()


sns.set_theme(style="ticks")

x = df["carat"]
y = df["price"]

# Graph 12 - jointplot (hex): carat, price
g = sns.jointplot(x=x, y=y, kind="hex", color="#4CB391")
g.figure.suptitle("sns.jointplot(x=carat, y=price, kind=hex)"  )
plt.show()


sns.set_theme(style="ticks")

# Graph 13 - jointplot (kde): carat, price, cut
g = sns.jointplot(
    data=df,
    x="carat", y="price", hue="cut",
    kind="kde",
)
g.figure.suptitle("sns.jointplot(x=carat, y=price, hue=cut, kind=kde)"  )
plt.show()


sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

pal = sns.cubehelix_palette(5, rot=-.25, light=.7)
g = sns.FacetGrid(df, row="cut", hue="cut", aspect=15, height=.5, palette=pal)

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

g.figure.subplots_adjust(hspace=-.25)

g.set_titles("")
g.set(yticks=[], ylabel="")
g.despine(bottom=True, left=True)
# Graph 14 - ridgeline plot: cut, price
g.figure.suptitle("sns.FacetGrid(df, row=cut, hue=cut) - kdeplot of price"  )
plt.show()


sns.set_theme(style="white")

d = df[["carat", "depth", "table", "price", "x", "y", "z"]]

corr = d.corr()

mask = np.triu(np.ones_like(corr, dtype=bool))

f, ax = plt.subplots(figsize=(11, 9))

cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Graph 15 - heatmap (correlation): carat, depth, table, price, x, y, z
g = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
g.figure.suptitle("sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, center=0, square=True)"  )
plt.show()