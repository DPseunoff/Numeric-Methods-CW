import numpy as np
from constants import *


def f1(x):
    return np.sin(2 * x)


def f2(x):
    if x <= 10:
        return np.cos(x) + np.sin(2 * x)
    else:
        return np.cos(x * 0.3) + np.sin(6 * x)


def f3(x):
    return np.sin(x ** 2)
