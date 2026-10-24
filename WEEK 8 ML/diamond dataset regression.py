import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\neskill\nexskill course ai bin\WEEK 8 ML\diamonds.csv")
print(df)

X_single = df["carat"].values.reshape(-1, 1)
Y_single = df["price"].values.reshape(-1, 1)

df.plot.scatter(x='carat', y='price', title='Scatter Plot of Diamonds....')
plt.savefig("diamonds_scatter.png", bbox_inches="tight")
plt.close()

df.info()
print(df.describe())
print(df.isnull().sum())

df.drop(columns=["Unnamed: 0"], inplace=True)

print("Zero values -> x:", (df["x"] == 0).sum(),
      "y:", (df["y"] == 0).sum(),
      "z:", (df["z"] == 0).sum())

# fix missing values (0 in x/y/z is not possible for a real diamond)
for col in ["x", "y", "z"]:
    df[col] = df[col].replace(0, np.nan)
    df[col] = df[col].fillna(df[col].median())

# handle outliers using IQR
for col in ["price", "x", "y", "z", "depth", "table"]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = np.clip(df[col], lower, upper)

# new feature: volume
df["volume"] = df["x"] * df["y"] * df["z"]

# separating X and y
X = df.drop(columns=["price"])
y = df["price"]

# numerical and categorical columns
categorical_cols = ["cut", "color", "clarity"]
numerical_cols = [c for c in X.columns if c not in categorical_cols]

print("Categorical columns:", categorical_cols)
print("Numerical columns:", numerical_cols)

# encoding categorical columns + scaling numerical columns
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(sparse_output=False), categorical_cols),
        ("num", StandardScaler(), numerical_cols),
    ]
)

X_processed = preprocessor.fit_transform(X)
print(X_processed.shape)

# train/test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_processed, y, test_size=0.2, random_state=25
)

# training models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

linear_regression = LinearRegression()
tree = DecisionTreeRegressor(random_state=25)

linear_regression.fit(X_train, y_train)
tree.fit(X_train, y_train)

lin_preds = linear_regression.predict(X_test)
tree_preds = tree.predict(X_test)

# evaluating models
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

model_preds = {
    "Linear Regression": lin_preds,
    "Decision Tree Regressor": tree_preds,
}

results = []
for model, preds in model_preds.items():
    mae = mean_absolute_error(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)
    print(f"{model} -> MAE: {mae:.2f}, RMSE: {rmse:.2f}, R2: {r2:.4f}")
    results.append({"Model": model, "MAE": round(mae, 2), "RMSE": round(rmse, 2), "R2_Score": round(r2, 4)})

# comparing models
comparison_df = pd.DataFrame(results).sort_values(by="R2_Score", ascending=False)
print(comparison_df.to_string(index=False))
print("Best performing model:", comparison_df.iloc[0]["Model"])

comparison_df.to_csv("diamonds_model_comparison.csv", index=False)