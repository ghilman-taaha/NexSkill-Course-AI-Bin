import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# data, carat and price (scaled)
diamonds_data = pd.read_csv(r'E:\neskill\NexSkill course AI bin\FINAL-ASSESSMENT\10-diamonds.csv', index_col='Unnamed: 0')
X = StandardScaler().fit_transform(diamonds_data[['carat', 'price']].values)

plt.scatter(X[:, 0], X[:, 1], s=20);
plt.show()


kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)


plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=20, cmap='summer')
centers = kmeans.cluster_centers_
color = np.array(['blue', 'hotpink', 'black', 'green'])

plt.scatter(centers[:, 0], centers[:, 1], c=color  , s=100, alpha=0.9);
plt.show()

wait = input("Hello")