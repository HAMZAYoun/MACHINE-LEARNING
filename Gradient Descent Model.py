# Gradient Descent 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
n = 300
X= np.random.normal(size=250, scale=0.25)
Y = 0.5*X + 0.7*np.random.normal(size=250, scale=0.25)
Theta0 = 0
Theta1 = 0
Alfa = 0.01
iterations = 10000
for i in range(iterations): 
    Yhat = Theta0*X + Theta1  
    Theta0 = Theta0 -  Alfa * (-2/n) * sum(X * (Y - Yhat))
    Theta1 = Theta1 -  Alfa * (-2/n) * sum(Y - Yhat)     
Yhat = Theta0*X + Theta1
plt.plot(X, Yhat, color='red')
plt.scatter(X,Y)
plt.rcParams['figure.figsize'] = (15.0, 5.0)
