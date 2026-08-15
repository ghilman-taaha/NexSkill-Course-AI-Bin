import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv')

# ==================================================
# Graph 1: lmplot - Assessed Value vs Sale Amount (Top 4 Towns)
# ==================================================
sns.set_theme(style="ticks")

dffilter1 = df.query('Town == "Bristol" or Town == "East Hartford" or Town == "Branford" or Town == "Danbury"')

sns.lmplot(
    data=dffilter1, x="Assessed Value", y="Sale Amount", col="Town", hue="Town",
    col_wrap=2, palette="muted", ci=None,
    height=4, scatter_kws={"s": 50, "alpha": 1}
)
plt.show()

# ==================================================
# Graph 2: displot - Sale Amount distribution by Residential Type
# ==================================================
sns.set_theme(style="darkgrid")

dffilter2 = df.query('`Property Type` == "Residential"')

sns.displot(
    dffilter2, x="Sale Amount", col="Residential Type",
    binwidth=50000, height=3, facet_kws=dict(margin_titles=True),
)
plt.show()

# ==================================================
# Graph 3: relplot - Assessed Value vs Sale Amount
# ==================================================
sns.set_theme(style="ticks")

dffilter3 = df.query('`Sale Amount` > 200000 or `Property Type` == "Commercial"')
palette = sns.color_palette("rocket_r")

sns.relplot(
    data=dffilter3,
    x="Assessed Value", y="Sale Amount",
    hue="Property Type", size="Sales Ratio", col="Property Type",
    kind="scatter", palette=palette,
    height=5, aspect=.75, facet_kws=dict(sharex=False),
)
plt.show()

# ==================================================
# Graph 4: violinplot - Sale Amount by Town split by Property Type
# ==================================================
sns.set_theme(style="dark")

dffilter4 = df.query('Town == "Bristol" or Town == "East Hartford" or Town == "Branford" or Town == "Danbury" or Town == "Greenwich"')

sns.violinplot(data=dffilter4, x="Town", y="Sale Amount", hue="Property Type",
               inner="quart", fill=False)
plt.show()