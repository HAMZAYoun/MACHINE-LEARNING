# Stochastic Gradient Descent "SGD"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
n = 350
X = np.random.normal(size=400, scale=0.75)
Y = 0.5* X +12.78*np.random.normal(size=400, scale=0.75)
Theta0 = 0
Theta1 = 0
Alfa = 0.01
iterations = 10000
for i in range(iterations): 
  for j in range(n):
    Yhat = Theta0*X[j] + Theta1  
    Theta0 = Theta0 -  Alfa * (-2/n) * (X[j] * (Y[j] - Yhat))
    Theta1 = Theta1 -  Alfa * (-2/n) * (Y[j] - Yhat)     
Yhat = Theta0*X+ Theta1
plt.plot(X, Yhat, color='red')
plt.scatter(X,Y)
plt.rcParams['figure.figsize'] = (20.0, 5.0)
