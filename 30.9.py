from __future__ import division, print_function, unicode_literals
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as matplotlib

# np.random.seed(5)
# x = np.random.randn(1000, 1) * 5
# y = 2+5*x+.2*np.random.randn(1000, 1)

# one = np.ones((x.shape[0], 1))
# xbar = np.concatenate((one, x), axis=1)


# a = np.dot(xbar.T, xbar)
# b = np.dot(xbar.T, y)
# w_lr = np.dot(np.linalg.pinv(a), b)
# print('w = ', w_lr.T)

# w = w_lr
# w_0 = w[0][0]
# w_1 = w[1][0]
# x0 = np.linspace(0, 1, 2, endpoint=True)
# y0 = w_0+w_1*x0

# plt.plot(x.T, y.T, 'b.')
# plt.plot(x0, y0, 'y', linewidth=2)
# plt.axis([0, 1, 0, 10])
# plt.show()


# np.random.seed(2)
# x = 5 -10*np.random.randn(1000, 1)
# y = 2+3*x+2*x*x+5-10*np.random.randn(1000, 1)

# one = np.ones((x.shape[0], 1))
# xbar = np.concatenate((one, x), axis=1)


# a = np.dot(xbar.T, xbar)
# b = np.dot(xbar.T, y)
# w_lr = np.dot(np.linalg.pinv(a), b)
# print('w = ', w_lr.T)

# w = w_lr
# w_0 = w[0][0]
# w_1 = w[1][0]
# w_2=  w[2][0]
# x0 = np.linspace(0, 1, 2, endpoint=True)
# y0 = w_0+w_1*x0+w_2*x0*x0

# plt.plot(x.T, y.T, 'b.')
# plt.plot(x0, y0, 'r', linewidth=2)
# plt.axis([0, 1, 0, 10])
# plt.show()
