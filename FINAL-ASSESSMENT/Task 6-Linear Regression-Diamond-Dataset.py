import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv(r'E:\neskill\NexSkill course AI bin\FINAL-ASSESSMENT\10-diamonds.csv', index_col='Unnamed: 0')

print(df)
print("df.shape:", df.shape)

df.plot.scatter(x='carat', y='price', title='Scatter Plot of carat and price')
plt.show()

print("df.corr():")
print(df.corr(numeric_only=True))

print("df.describe():")
print(df.describe())

print("df['price']:")
print(df['price'])
print("df['carat']:")
print(df['carat'])

y = df['price'].values.reshape(-1, 1)
X = df['carat'].values.reshape(-1, 1)

print("y:", y)
print("X:", X)
print(df['carat'].values)
print(df['carat'].values.shape)
print(X.shape)

SEED = 42

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)

print(X_train)
print(y_train)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.intercept_)
print(regressor.coef_)


def calc(slope, intercept, carat):
    return slope * carat + intercept


score = calc(regressor.coef_, regressor.intercept_, 1.5)
print(score)

score = regressor.predict([[1.5]])
print(score)

y_pred = regressor.predict(X_test)

df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')

dffilter = df

sns.set(style="whitegrid")

# Graph 1 - displot hist (x=cut, y=price, hue=color)
g = sns.displot(data=dffilter, x="cut", y="price", hue="color", kind='hist')
g.figure.suptitle("sns.displot(data=dffilter, x=cut, y=price, hue=color, kind='hist')")
plt.show()

# Graph 2 - displot kde (x=price, y=carat)
g = sns.displot(data=dffilter, x="price", y="carat", kind='kde')
g.figure.suptitle("sns.displot(data=dffilter, x=price, y=carat, kind='kde')")
plt.show()

# Graph 3 - kdeplot (x=price)
g = sns.kdeplot(data=dffilter, x="price")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=price)")
plt.show()

# Graph 4 - histplot stacked (x=cut, y=price, hue=cut)
g = sns.histplot(data=dffilter, x='cut', y='price', hue='cut', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='cut', y='price', hue='cut', multiple=stack)")
plt.show()

# Graph 5 - scatterplot (x=cut, y=price)
g = sns.scatterplot(x='cut', y='price', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='cut', y='price', data=dffilter)")
plt.show()

# Graph 6 - lineplot (x=cut, y=price)
g = sns.lineplot(data=dffilter, x="cut", y="price")
g.figure.suptitle("sns.lineplot(data=dffilter, x=cut, y=price)")
plt.show()

# Graph 7 - barplot (x=cut, y=price)
g = sns.barplot(data=dffilter, x="cut", y="price", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=cut, y=price, legend=False)")
plt.show()

# Graph 8 - catplot (x=cut, y=price)
g = sns.catplot(data=dffilter, x="cut", y="price")
g.figure.suptitle("sns.catplot(data=df, x=cut, y=price)")
plt.show()

# Graph 9 - heatmap (pivot of price by cut)
glue = dffilter.pivot(columns="cut", values="price")
g = sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue) - glue = dffilter.pivot(columns=cut, values=price)")
plt.show()

sns.set_theme(style="ticks", palette="pastel")

# Graph 10 - boxplot (x=cut, y=price, hue=color)
g = sns.boxplot(x="cut", y="price", hue="color", data=df)
sns.despine(offset=10, trim=True)
g.figure.suptitle("sns.boxplot(x=cut, y=price, hue=color, data=df)")
plt.show()

sns.set_theme(style="dark")

# Graph 11 - violinplot (x=cut, y=price, hue=color, colors D and J)
g = sns.violinplot(data=df[df["color"].isin(["D", "J"])], x="cut", y="price", hue="color",
                   split=True, inner="quart", fill=False,
                   palette={"D": "g", "J": ".35"})
g.figure.suptitle("sns.violinplot(x=cut, y=price, hue=color, split=True)")
plt.show()

sns.set_theme(style="ticks")

x = df["carat"]
y = df["price"]

# Graph 12 - jointplot hex (x=carat, y=price)
g = sns.jointplot(x=x, y=y, kind="hex", color="#4CB391")
g.figure.suptitle("sns.jointplot(x=carat, y=price, kind=hex)")
plt.show()

# Graph 13 - jointplot kde (x=carat, y=price, hue=cut)
g = sns.jointplot(data=df, x="carat", y="price", hue="cut", kind="kde")
g.figure.suptitle("sns.jointplot(x=carat, y=price, hue=cut, kind=kde)")
plt.show()

sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})


# Graph 15 - correlation heatmap (carat, depth, table, price, x, y, z)
d = df[["carat", "depth", "table", "price", "x", "y", "z"]]
corr = d.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(230, 20, as_cmap=True)

g = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, center=0,
               square=True, linewidths=.5, cbar_kws={"shrink": .5})
g.figure.suptitle("sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, center=0, square=True)")
plt.show()