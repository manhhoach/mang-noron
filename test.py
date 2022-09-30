from __future__ import division, print_function, unicode_literals
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as matplotlib

# y=(x+1)^2, x=[-5, 5], 1000 points

np.random.seed(2)  
x = np.random.rand(1000, 1)*10-5
y = 1 + 2*x + x*x + .2*(np.random.rand(1000, 1)*10-5)

one = np.ones((x.shape[0], 2))  
xbar = np.concatenate((one, x), axis=1)  

a = np.dot(xbar.T, xbar)  
b = np.dot(xbar.T, y)
w = np.dot(np.linalg.pinv(a), b)  

print('Ta co w = ', w.T)


w0 = w[0][0]
w1 = w[1][0]
w2 = w[2][0]

x0 = np.linspace(-5, 5, 1000, endpoint=True)  
y0 = w0 + w1*x0 + w2*x0*x0

plt.plot(x.T, y.T, 'b.')
plt.plot(x0, y0, 'y', linewidth=2)
plt.axis([-10, 10, -10, 10])  
plt.show()
