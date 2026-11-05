import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# load data
path_to_file = r'E:\neskill\NexSkill course AI bin\FINAL-ASSESSMENT\10-diamonds.csv'
df = pd.read_csv(path_to_file, index_col='Unnamed: 0')

print("df:  \n", df)

print("df.shape: \n" , df.shape)

print("df.describe().round(2).T:    \n",df.describe().round(2).T)


import seaborn as sns

variables = ['carat', 'depth', 'table', 'x', 'y', 'z']

# regression plots
for var in variables:
    plt.figure()
    sns.regplot(x=var, y='price', data=df).set(title=f'Regression plot of {var} and price');
    plt.show()

read = input("Wait here: \n")


# correlation heatmap
plt.figure()
correlations = df.corr(numeric_only=True)
print("correlations...\n" , correlations)
g = sns.heatmap(correlations, annot=True).set(title='Heat map of Diamonds Data - Pearson Correlations')
plt.show()
read = input("Wait for me....")

# features and target
y = df['price']
X = df[['carat', 'depth', 'table', 'x', 'y', 'z']]

SEED = 200
# train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=SEED)

print("X.shape # (53940, 6):     \n", X.shape )   


# model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)

print("regressor.intercept_......\n", regressor.intercept_)

print("regressor.coef_ " , regressor.coef_)

feature_names = X.columns
model_coefficients = regressor.coef_

coefficients_df = pd.DataFrame(data = model_coefficients, 
                              index = feature_names, 
                              columns = ['Coefficient value'])
print(coefficients_df)


# predictions
y_pred = regressor.predict(X_test)


results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("Actual vs Predicted.....\n" , results)


# errors
from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')


# r2
actual_minus_predicted = sum((y_test - y_pred)**2)
actual_minus_actual_mean = sum((y_test - y_test.mean())**2)
r2 = 1 - actual_minus_predicted/actual_minus_actual_mean
print('R²:', r2)

print(" R2 score method...\n", regressor.score(X_test, y_test))