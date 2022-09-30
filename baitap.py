from __future__ import division, print_function, unicode_literals
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as matplotlib


np.random.seed() 

x = np.random.rand(1000, 1)*10-5
y = 1 + 2*x + x*x + (0.2*np.random.rand(1000, 1)*10-5)


one = np.ones((x.shape[0], 1)) 
xbar = np.concatenate((one, x), axis=1)

a = np.dot(xbar.T, xbar)  
b = np.dot(xbar.T, y)
w_lr = np.dot(np.linalg.pinv(a), b)  # a^-1*b

print('Ta co w = ', w_lr.T)

w_0 = w_lr[0][0]
w_1 = w_lr[1][0]

x0 = np.linspace(-5, 5, 1000, endpoint=True)
y0 = w_0*x0 + w_1*x0*x0

plt.plot(x.T, y.T, 'b.')
plt.plot(x0, y0, 'y', linewidth=2)
plt.axis([-10, 10, -10, 10]) # set x,y min max
plt.show()
