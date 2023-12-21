import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("final-project/air_quality_data.csv", delimiter=";")

x = data["Time"].values
y = data["S1(CO)"].values

print(x)
print(y)
x = x.reshape(-1,1)

model = LinearRegression().fit(x, y)

coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x, y)
print(coef, intercept, r_squared)

print(f"Model's Linear Equation: y= {coef}x+{intercept}")
print(f"R Squared Value: {r_squared}")

plt.figure(figsize=(6, 4))

plt.scatter(x,y)
plt.xlabel("Time")
plt.ylabel("NMHC(GT)")
plt.title("NHMC(GT) Concentration by Time")
plt.plot(x,coef*x+intercept, c="r", label="Line of best fit")

plt.show()