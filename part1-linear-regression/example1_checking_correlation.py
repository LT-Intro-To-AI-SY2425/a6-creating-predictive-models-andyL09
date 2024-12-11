import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# opens CSV file kinda like a import statement
# sets x and y values for the headers and the values after them on the columns for the 
data = pd.read_csv("part1-linear-regression/chirping_data.csv")
x = data["Temp"]
y = data["Chirps"]

# sets the size of the graph
plt.figure(figsize=(6,4))

# creates a scatter plot and labels the axes
plt.scatter(x,y)
plt.xlabel("Temperature °F")
plt.ylabel("Chirps per Minute")
plt.title("Cricket Chirps by Temperature")

# prints the correlation coefficient
print(f"Correlation between Temperature and Chirps/Min: {x.corr(y)}")

# show the plot
plt.show()