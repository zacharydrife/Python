import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data
housing_data = pd.read_csv('housing_data.csv')
X = housing_data[['Sq ft', 'Burglaries']]
y = housing_data['Rent']

# Create the model
reg = LinearRegression()

# Train the model
reg.fit(X, y)

square_footage = int(input('Enter square footage: '))
number_of_burglaries = int(input('Enter number of burglaries: '))

# Provide feature names explicitly when making predictions
y_pred = reg.predict(pd.DataFrame({'Sq ft': [square_footage], 'Burglaries': [number_of_burglaries]}))

print(y_pred)
