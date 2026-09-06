import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\neskill\NexSkill course AI bin\WEEK 8 ML\housing.csv")

print(df.shape)
print(df.head())
df.info()
print(df.describe())
print(df.corr(numeric_only=True))
print(df.isnull().sum())

df["median_house_value"].plot.hist()
plt.title("Distribution of Median House Value")
plt.savefig("housing_value_hist.png", bbox_inches="tight")
plt.close()

# ---------------- MISSING VALUES ----------------
df["total_bedrooms"] = df["total_bedrooms"].fillna(df["total_bedrooms"].median())

# ---------------- OUTLIERS (IQR method) ----------------
for col in ["total_rooms", "total_bedrooms", "population", "households"]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = np.clip(df[col], lower, upper)

print(df.isnull().sum())

# ---------------- FEATURE ENGINEERING ----------------
df["rooms_per_household"] = df["total_rooms"] / df["households"]

# ---------------- SEPARATE X AND y ----------------
X = df.drop(columns=["median_house_value"])
y = df["median_house_value"]

# ---------------- NUMERICAL AND CATEGORICAL COLUMNS ----------------
categorical_cols = ["ocean_proximity"]
numerical_cols = [c for c in X.columns if c not in categorical_cols]

print("Categorical columns:", categorical_cols)
print("Numerical columns:", numerical_cols)

# ---------------- ENCODING ----------------
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

# ---------------- TRAIN / TEST SPLIT ----------------
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_processed, y, test_size=0.2, random_state=42
)

print(f"Train size: {round(len(X_train) / len(X_processed) * 100)}%")
print(f"Test size: {round(len(X_test) / len(X_processed) * 100)}%")

# ---------------- TRAIN MODELS ----------------
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

linear_regression = LinearRegression()
tree = DecisionTreeRegressor(random_state=25)

linear_regression.fit(X_train, y_train)
tree.fit(X_train, y_train)

lin_preds = linear_regression.predict(X_test)
tree_preds = tree.predict(X_test)

# SVR needs y scaled too, and dataset is large so train on a sample
y_scaler = StandardScaler()
y_train_scaled = y_scaler.fit_transform(y_train.values.reshape(-1, 1)).ravel()

sample_size = min(5000, len(X_train))
rng = np.random.RandomState(25)
sample_idx = rng.choice(len(X_train), size=sample_size, replace=False)

svr = SVR(kernel="rbf", C=100)
svr.fit(X_train[sample_idx], y_train_scaled[sample_idx])
svr_preds = y_scaler.inverse_transform(svr.predict(X_test).reshape(-1, 1)).ravel()

# ---------------- EVALUATE ----------------
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

model_preds = {
    "Linear Regression": lin_preds,
    "Support Vector Regressor": svr_preds,
    "Decision Tree Regressor": tree_preds,
}

results = []
for model, preds in model_preds.items():
    mae = mean_absolute_error(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, preds)
    print(f"{model} -> MAE: {mae:.2f}, RMSE: {rmse:.2f}, R2: {r2:.4f}")
    results.append({"Model": model, "MAE": round(mae, 2), "RMSE": round(rmse, 2), "R2_Score": round(r2, 4)})

comparison_df = pd.DataFrame(results).sort_values(by="R2_Score", ascending=False)
print(comparison_df.to_string(index=False))
print("Best performing model:", comparison_df.iloc[0]["Model"])

comparison_df.to_csv("housing_model_comparison.csv", index=False)