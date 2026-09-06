import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\neskill\NexSkill course AI bin\WEEK 8 ML\heart_disease_hf.csv")

print(df.shape)
print(df.head())
df.info()
print(df.describe())
print(df.isnull().sum())

plt.figure(figsize=(6, 4))
df["target"].value_counts().plot(kind="bar")
plt.title("Heart Disease Count (0 = No Disease, 1 = Disease)")
plt.savefig("heart_target_count.png", bbox_inches="tight")
plt.close()

# fix bad thal values (2 rows have numeric codes instead of category names)
valid_thal = ["normal", "fixed", "reversible"]
df.loc[~df["thal"].isin(valid_thal), "thal"] = df["thal"].mode()[0]

# cap chol outliers
Q1 = df["chol"].quantile(0.25)
Q3 = df["chol"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df["chol"] = np.clip(df["chol"], lower, upper)

df["high_chol"] = (df["chol"] > 240).astype(int)

X = df.drop(columns=["target"])
y = df["target"]

nominal_features = ["thal"]
numeric_features = [c for c in X.columns if c not in nominal_features]

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer(
    transformers=[
        ("nom", OneHotEncoder(sparse_output=False), nominal_features),
        ("num", StandardScaler(), numeric_features),
    ]
)

X_scaled = preprocessor.fit_transform(X)

from sklearn.model_selection import train_test_split

X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(
    X_scaled, y, train_size=0.7, random_state=25
)

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

logistic_regression = LogisticRegression(max_iter=1000)
svm = SVC()
tree = DecisionTreeClassifier(random_state=25)

logistic_regression.fit(X_train_scaled, y_train)
svm.fit(X_train_scaled, y_train)
tree.fit(X_train_scaled, y_train)

log_reg_preds = logistic_regression.predict(X_test_scaled)
svm_preds = svm.predict(X_test_scaled)
tree_preds = tree.predict(X_test_scaled)

from sklearn.metrics import classification_report, accuracy_score, f1_score, confusion_matrix

model_preds = {
    "Logistic Regression": log_reg_preds,
    "Support Vector Machine": svm_preds,
    "Decision Tree": tree_preds,
}

results = []
for model, preds in model_preds.items():
    print(f"{model} Results:\n{classification_report(y_test, preds)}")
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds)
    results.append({"Model": model, "Accuracy": round(acc, 4), "F1-Score": round(f1, 4)})

comparison_df = pd.DataFrame(results).sort_values(by="F1-Score", ascending=False)
print(comparison_df.to_string(index=False))

best_model = comparison_df.iloc[0]["Model"]
print("Best performing model:", best_model)

best_preds = model_preds[best_model]

comparison_df.to_csv("heart_model_comparison.csv", index=False)