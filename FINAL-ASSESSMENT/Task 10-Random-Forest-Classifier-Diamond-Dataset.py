import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

# load data
path = r'E:\neskill\NexSkill course AI bin\FINAL-ASSESSMENT\10-diamonds.csv'
diamonds_data = pd.read_csv(path, index_col='Unnamed: 0')

# target, price in 5 groups
diamonds_data['target'] = pd.qcut(diamonds_data['price'], 5, labels=['Low', 'Medium', 'High', 'Premium', 'Luxury'])

diamonds_data = diamonds_data.dropna(subset=['target'])

X = diamonds_data[['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']]
y = diamonds_data['target']

# text to numbers
X.loc[:, 'cut'] = X['cut'].map({'Fair': '0', 'Good': '1', 'Very Good': '2', 'Premium': '3', 'Ideal': '4'})
X.loc[:, 'color'] = X['color'].map({'J': '0', 'I': '1', 'H': '2', 'G': '3', 'F': '4', 'E': '5', 'D': '6'})
X.loc[:, 'clarity'] = X['clarity'].map({'I1': '0', 'SI2': '1', 'SI1': '2', 'VS2': '3', 'VS1': '4', 'VVS2': '5', 'VVS1': '6', 'IF': '7'})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

rf_classifier.fit(X_train, y_train)

y_pred = rf_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_rep)

sample = X_test.iloc[0:1]
prediction = rf_classifier.predict(sample)

sample_dict = sample.iloc[0].to_dict()
print(f"\nSample Diamond: {sample_dict}")
print(f"Predicted Price Group: {prediction[0]}")