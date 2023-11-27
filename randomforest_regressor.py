import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# Load the dataset
data = pd.DataFrame({
    'Position': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Level': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary': [45000, 50000, 60000, 80000, 110000, 150000, 200000, 300000, 500000, 1000000]
})

# Separate the features (Level) and the target variable (Salary)
X = data[['Level']]
y = data['Salary']

# Create and train the Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X, y)

# Predict the salary for a given position level
position_level = np.array([[7.5]])  # Example: Predict salary for position level 7.5
predicted_salary = rf_regressor.predict(position_level)
print(f"Predicted Salary for Position Level 7.5: ${predicted_salary[0]:,.2f}")

# Visualize the Random Forest Regression results
X_grid = np.arange(min(X['Level']), max(X['Level']), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color='red')
plt.plot(X_grid, rf_regressor.predict(X_grid), color='blue')
plt.title('Random Forest Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
