import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\neskill\NexSkill course AI bin\WEEK 8 ML\insurance_kaggle.csv")

print(df.shape)
print(df.head())
df.info()
print(df.describe())
print(df.isnull().sum())

plt.figure(figsize=(6, 4))
df["charges"].plot(kind="hist", bins=30)
plt.title("Distribution of Insurance Charges")
plt.savefig("insurance_charges_dist.png", bbox_inches="tight")
plt.close()

plt.figure(figsize=(6, 4))
plt.boxplot(df["charges"])
plt.title("Charges - Outlier Check")
plt.savefig("insurance_charges_boxplot.png", bbox_inches="tight")
plt.close()

# no missing values in this dataset

# handle outliers in bmi (IQR method)
Q1 = df["bmi"].quantile(0.25)
Q3 = df["bmi"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df["bmi"] = np.clip(df["bmi"], lower, upper)

X = df.drop(columns=["charges"])
y = df["charges"]

nominal_features = ["sex", "smoker", "region"]
numeric_features = [c for c in X.columns if c not in nominal_features]

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer(
    transformers=[
        ("nom", OneHotEncoder(sparse_output=False, drop="if_binary"), nominal_features),
        ("num", StandardScaler(), numeric_features),
    ]
)

X_scaled = preprocessor.fit_transform(X)

from sklearn.model_selection import train_test_split

X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(
    X_scaled, y, train_size=0.7, random_state=25
)

from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

linear_regression = LinearRegression()
tree_reg = DecisionTreeRegressor(random_state=25)

linear_regression.fit(X_train_scaled, y_train)
tree_reg.fit(X_train_scaled, y_train)

lin_preds = linear_regression.predict(X_test_scaled)
tree_preds = tree_reg.predict(X_test_scaled)

# SVR needs the target scaled too, otherwise it performs badly
y_scaler = StandardScaler()
y_train_scaled = y_scaler.fit_transform(y_train.values.reshape(-1, 1)).ravel()

svr = SVR(kernel="rbf", C=100)
svr.fit(X_train_scaled, y_train_scaled)
svr_preds = y_scaler.inverse_transform(svr.predict(X_test_scaled).reshape(-1, 1)).ravel()

from sklearn.metrics import mean_squared_error, r2_score

model_preds = {
    "Linear Regression": lin_preds,
    "Support Vector Regressor": svr_preds,
    "Decision Tree Regressor": tree_preds,
}

results = []
for model, preds in model_preds.items():
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)
    print(f"{model} -> RMSE: {rmse:.2f}, R2: {r2:.4f}")
    results.append({"Model": model, "RMSE": round(rmse, 2), "R2_Score": round(r2, 4)})

comparison_df = pd.DataFrame(results).sort_values(by="R2_Score", ascending=False)
print(comparison_df.to_string(index=False))
print("Best performing model:", comparison_df.iloc[0]["Model"])

comparison_df.to_csv("insurance_model_comparison.csv", index=False)