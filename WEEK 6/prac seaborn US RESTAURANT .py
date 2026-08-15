import seaborn as sns
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv('FastFoodRestaurants.csv')

# Data cleaning: USA ka longitude hamesha negative hota hai (galat entries hata rahe hain)
df = df.query('longitude < 0 and longitude > -180')

# ==================================================
# Graph 1: lmplot - Longitude vs Latitude (Top 4 Brands)
# ==================================================
sns.set_theme(style="ticks")

dffilter1 = df.query('name == "McDonald\'s" or name == "Burger King" or name == "Taco Bell" or name == "Wendy\'s"')

sns.lmplot(
    data=dffilter1, x="longitude", y="latitude", col="name", hue="name",
    col_wrap=2, palette="muted", ci=None,
    height=4, scatter_kws={"s": 50, "alpha": 1}
)
plt.show()

# ==================================================
# Graph 2: displot - Latitude distribution by Brand
# ==================================================
sns.set_theme(style="darkgrid")

dffilter2 = df.query('name == "McDonald\'s" or name == "Burger King" or name == "Taco Bell"')

sns.displot(
    dffilter2, x="latitude", col="name",
    binwidth=3, height=3, facet_kws=dict(margin_titles=True),
)
plt.show()

# ==================================================
# Graph 3: relplot - Longitude vs Latitude
# ==================================================
sns.set_theme(style="ticks")

dffilter3 = df.query('name == "McDonald\'s" or name == "Burger King"')
palette = sns.color_palette("rocket_r")

sns.relplot(
    data=dffilter3,
    x="longitude", y="latitude",
    hue="name", col="name",
    kind="scatter", palette=palette,
    height=5, aspect=.75, facet_kws=dict(sharex=False),
)
plt.show()

# ==================================================
# Graph 4: violinplot - Latitude by Brand
# ==================================================
sns.set_theme(style="dark")

dffilter4 = df.query('name == "McDonald\'s" or name == "Burger King" or name == "Taco Bell" or name == "Wendy\'s" or name == "Arby\'s"')

sns.violinplot(data=dffilter4, x="name", y="latitude",
               inner="quart", fill=False)
plt.show()