from math import radians
import numpy as np
import matplotlib.pyplot as plt
#from __future__ import division, print_function


def main():
    x = np.arange(0, radians(1800), radians(12))
    y = np.arange(0, radians(1500), radians(10))
    plt.plot(x, np.cos(x), 'r')
    plt.plot(x, np.sin(y), 'b')
    plt.show()

main()

