import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"E:\neskill\NexSkill course AI bin\WEEK 8 ML\heart_disease_hf.csv")

# ---------------- EDA (
print(df.head())
df.info()
print(df.describe())
print(df.tail())

# ---------------- EDA 
print(df['target'].value_counts())
print(df['target'].value_counts(normalize=True))
df['target'].plot.hist()
plt.savefig("heart_target_hist.png", bbox_inches="tight")
plt.close()

# ---------------- ENCODING 
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['thal_encoded'] = le.fit_transform(df['thal'])
print("thal labels mapping:", dict(zip(le.classes_, le.transform(le.classes_))))

# ---------------- X and y 
feature_cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal_encoded']
X = df[feature_cols].copy()
y = df['target'].copy()

# ---------------- SCALING 
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X.values)

# ---------------- TRAIN/TEST SPLIT 
from sklearn.model_selection import train_test_split

X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(
    X_scaled, y, train_size=.7, random_state=25
)

print(f"Train size: {round(len(X_train_scaled) / len(X) * 100)}%")
print(f"Test size: {round(len(X_test_scaled) / len(X) * 100)}%")

# ---------------- TRAIN MODELS 
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

logistic_regression = LogisticRegression()
svm = SVC()
tree = DecisionTreeClassifier()

logistic_regression.fit(X_train_scaled, y_train)
svm.fit(X_train_scaled, y_train)
tree.fit(X_train_scaled, y_train)

log_reg_preds = logistic_regression.predict(X_test_scaled)
svm_preds = svm.predict(X_test_scaled)
tree_preds = tree.predict(X_test_scaled)

# ---------------- CLASSIFICATION REPORT 
from sklearn.metrics import classification_report

model_preds = {
    "Logistic Regression": log_reg_preds,
    "Support Vector Machine": svm_preds,
    "Decision Tree": tree_preds
}

for model, preds in model_preds.items():
    print(f"{model} Results:\n{classification_report(y_test, preds)}", sep="\n\n")

# ---------------- CONFUSION MATRIX
from sklearn import metrics

for model, preds in model_preds.items():
    cnf_matrix = metrics.confusion_matrix(y_test, preds)
    plt.figure()
    sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu", fmt='g')
    plt.title(f'Confusion matrix - {model}')
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    plt.savefig(f"heart_confusion_{model.replace(' ', '_')}.png", bbox_inches="tight")
    plt.close()

# ---------------- DECISION TREE VISUALIZATION 
from sklearn.tree import export_graphviz
from six import StringIO
import pydotplus

dot_data = StringIO()
export_graphviz(tree, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True, feature_names=feature_cols,
                class_names=['0', '1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('heart_tree.png')

# ---------------- ACCURACY 
print("Accuracy:", metrics.accuracy_score(y_test, tree_preds))