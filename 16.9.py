from __future__ import division, print_function, unicode_literals
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def cost(x):
    return x**2+5*np.sin(x)

def grad(x):
    return 2*x+5*np.cos(x)

def gd(eta, x0):
    x = [x0]
    for i in range(100):
        x_new = x[-1]-eta*grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x, i)

(x1, i1) = gd(0.1, -5)
(x2, i2) = gd(0.1, 5)

# print(x1, i1)

# print('x=%f,cost=%f, tai %d vong lap' % (x1[-1], cost(x1[-1]), i1))
# print('x=%f,cost=%f, tai %d vong lap' % (x2[-1], cost(x2[-1]), i2))


def draw(x1, ids, filename, nrows=2, ncols=4, start=-5.5):
    x0=np.linspace(start, 5.5, 1000)
    y0=cost(x0)
    width=4*ncols
    height=4*nrows
    plt.close('all')
    axs= plt.subplot(nrows, ncols, figsize=(width, height))
    with PdfPages(filename) as pdf:
        for i,k in (ids):
            r=i//ncols
            c=i%ncols
            x=x1[ids[i]]
            y=cost(x)
            str='iter {}/{}, grad = {:.3f}'.format(ids[i], len(x1)-1, grad(x))
            axs[r, c].plot(x0, y0, 'b')
            axs[r, c].set_xlabel(str, fontsize=13)
            axs[r, c].plot(x, y, 'kh', markersize=8, markeredgecolor='y')
          #  axs[r, c].plot()
            axs[r, c].tick_params(axis='both', which='major', labelsize=13)
        pdf.savefig(bbox_inches='tight')
        plt.show()


draw(x1, i1, 'test')