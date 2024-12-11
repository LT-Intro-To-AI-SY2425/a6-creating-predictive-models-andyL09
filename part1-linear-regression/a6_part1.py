import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#opens CSV file kinda like a import statement
# sets x and y values for the headers and the values after them on the columns for the 
data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
#addressing x and y based on value headers
x = data["Age"].values
y = data["Blood Pressure"].values

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)

# Create the model
model = LinearRegression().fit(x, y)
# using the "lilnear regrission" func will make this easier for us somehow
# im pretty sure it does some of the math for us or something
# the fit xy part just alings the data from CSV to the x an y axises i think


# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coef = round(float(model.coef_[0]), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x, y)

# Print out the linear equation and r squared value
#print(f"Model's Linear Equation: y = {coef}x + {intercept}")
#print(f"R Squared value: {r_squared}")
#print(f"Prediction when x is {x_predict}: {prediction}")

# Predict the the blood pressure of someone who is 43 years old.
x_predict = 43
prediction = model.predict([[x_predict]])

# Print out the prediction
print(f"Model's Linear Equation: y = {coef}x + {intercept}")
print(f"R Squared value: {r_squared}")
print(f"Prediction when x is {x_predict}: {prediction}")

#this makes the scatter plot and the line of best fit
plt.figure(figsize=(6,4)) #sets plot size

# Scatter plot of the original data
plt.scatter(x, y, c="purple", label="Data Points")

# makes line of best fit
# Generate y-values for the line based on the model's equation
line_y = coef * x + intercept 
plt.plot(x, line_y, c="red", label="Line of Best Fit")

# Adds predicted points to plot
plt.scatter(x_predict, prediction, c="blue", label=f"Prediction at x={x_predict}")

# axis and title
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure vs. Age")

plt.legend()

plt.show()