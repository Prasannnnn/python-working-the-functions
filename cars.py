import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn import metrics
import numpy as np
import pickle

# Load the dataset
df = pd.read_csv('car data.csv')

# Display dataset shape
print(df.shape)

# Display unique values for categorical columns
print(df['Seller_Type'].unique())
print(df['Fuel_Type'].unique())
print(df['Transmission'].unique())
print(df['Owner'].unique())

# Check for missing values
print(df.isnull().sum())

# Display basic statistics
print(df.describe())

# Select relevant features
final_dataset = df[['Year', 'Selling_Price', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']]
final_dataset['Current Year'] = 2020
final_dataset['no_year'] = final_dataset['Current Year'] - final_dataset['Year']
final_dataset.drop(['Year', 'Current Year'], axis=1, inplace=True)
final_dataset = pd.get_dummies(final_dataset, drop_first=True)

# Display the processed dataset
print(final_dataset.head())

# Calculate and display the correlation matrix
corrmat = final_dataset.corr()
plt.figure(figsize=(20, 20))
sns.heatmap(corrmat, annot=True, cmap="RdYlGn")
plt.show()

# Split the data into features and target variable
X = final_dataset.iloc[:, 1:]
y = final_dataset.iloc[:, 0]

# Display unique values and first few rows of features and target variable
print(X['Owner'].unique())
print(X.head())
print(y.head())

# Feature Importance
model = ExtraTreesRegressor()
model.fit(X, y)
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(5).plot(kind='barh')
plt.show()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Define the parameter grid for Randomized Search CV
n_estimators = [int(x) for x in np.linspace(start=100, stop=1200, num=12)]
max_features = ['auto', 'sqrt']
max_depth = [int(x) for x in np.linspace(5, 30, num=6)]
min_samples_split = [2, 5, 10, 15, 100]
min_samples_leaf = [1, 2, 5, 10]

random_grid = {
    'n_estimators': n_estimators,
    'max_features': max_features,
    'max_depth': max_depth,
    'min_samples_split': min_samples_split,
    'min_samples_leaf': min_samples_leaf
}

print(random_grid)

# Perform Randomized Search CV
rf = RandomForestRegressor()
rf_random = RandomizedSearchCV(estimator=rf, param_distributions=random_grid, scoring='neg_mean_squared_error', n_iter=10, cv=5, verbose=2, random_state=42, n_jobs=1)
rf_random.fit(X_train, y_train)

# Display the best parameters and best score
print(rf_random.best_params_)
print(rf_random.best_score_)

# Make predictions and evaluate the model
predictions = rf_random.predict(X_test)
sns.distplot(y_test - predictions)
plt.scatter(y_test, predictions)
plt.show()

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

# Save the model to a file
with open('random_forest_regression_model.pkl', 'wb') as file:
    pickle.dump(rf_random, file)
