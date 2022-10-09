from __future__ import division, print_function, unicode_literals
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as matplotlib

np.random.seed(2)
x = np.random.rand(1000, 1)*10-5
y = 1-10*x + 0.2*np.random.randn(1000, 1)

one = np.ones((x.shape[0], 1))
Xbar = np.concatenate((one, x), axis=1)


def grad(w):
    N = Xbar.shape[0]
    return 1/N*Xbar.T.dot(Xbar.dot(w)-y)


def cost(w):
    N = Xbar.shape[0]
    return 0.5/N*np.linalg.norm(y-Xbar.dot(w), 2)**2


def num_gd(w, cost):
    eps = 1e-4
    g = np.zeros_like(w)
    for i in range(len(w)):
        w_p = w.copy()
        w_n = w.copy()
        w_p[i] =w_p[i]+eps
        w_n[i] = w_n[i]-eps

        g[i] = (cost(w_p)-cost(w_n))/(2*eps)
    return g


def gd(w_init, num_gd, eta):
    w = [w_init]
    for i in range(100):
        w_new = w[-1]-eta*grad(w[-1])
        if np.linalg.norm(grad(w_new)/len(w_new)) < 1e-3:
            break
        w.append(w_new)
    return (w, i)


w_init = np.array([[2], [1]])
(w1, it1) = gd(w_init, grad, 1)
print(w1[-1].T, it1+1)
