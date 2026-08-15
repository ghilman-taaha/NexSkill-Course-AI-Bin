import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('startup_growth_investment_data.csv')

# ==================================================
# Graph 1: lmplot - Investment vs Valuation (Top 4 Industries)
# ==================================================
sns.set_theme(style="ticks")

dffilter1 = df.query('Industry == "SaaS" or Industry == "Fintech" or Industry == "AI" or Industry == "Blockchain"')

sns.lmplot(
    data=dffilter1, x="Investment Amount (USD)", y="Valuation (USD)", col="Industry", hue="Industry",
    col_wrap=2, palette="muted", ci=None,
    height=4, scatter_kws={"s": 50, "alpha": 1}
)
plt.show()

# ==================================================
# Graph 2: displot - Growth Rate distribution by Industry
# ==================================================
sns.set_theme(style="darkgrid")

dffilter2 = df.query('Industry == "SaaS" or Industry == "Fintech" or Industry == "AI"')

sns.displot(
    dffilter2, x="Growth Rate (%)", col="Industry",
    binwidth=20, height=3, facet_kws=dict(margin_titles=True),
)
plt.show()

# ==================================================
# Graph 3: relplot - Investment vs Valuation (USA vs UK)
# ==================================================
sns.set_theme(style="ticks")

dffilter3 = df.query('Country == "USA" or Country == "UK"')
palette = sns.color_palette("rocket_r")

sns.relplot(
    data=dffilter3,
    x="Investment Amount (USD)", y="Valuation (USD)",
    hue="Country", size="Number of Investors", col="Country",
    kind="scatter", palette=palette,
    height=5, aspect=.75, facet_kws=dict(sharex=False),
)
plt.show()

# ==================================================
# Graph 4: violinplot - Growth Rate by Industry
# ==================================================
sns.set_theme(style="dark")

dffilter4 = df.query('Industry == "SaaS" or Industry == "Fintech" or Industry == "AI" or Industry == "Blockchain" or Industry == "EdTech"')

sns.violinplot(data=dffilter4, x="Industry", y="Growth Rate (%)",
               inner="quart", fill=False)
plt.show()