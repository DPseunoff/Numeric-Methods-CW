import numpy as np
from constants import *


def check_level(level):
    max_level = int(np.log2(M))
    if level is None:
        return max_level
    elif level < 0:
        raise ValueError("Значение уровня %d слишком мало. Минимальный допустимый уровень 0." % level)
    elif level > max_level:
        print(
            "Значение уровня {0} слишком велико. Будет использован максимальный уровень {1}.".format(level, max_level))
        return max_level
    return level


def dwt(data):
    size = len(data) // 2
    cA = np.zeros(size)
    cD = np.zeros(size)

    for i, j in zip(range(0, len(data), 2), range(size)):
        c = 2 * (data[i] + data[i + 1]) / np.sqrt(M)
        cA[j] = c

    for i, j in zip(range(0, len(data), 2), range(size)):
        c = 2 * (data[i] - data[i + 1]) / np.sqrt(M)
        cD[j] = c

    return cA, cD


def waveDecompose(data, level = None):
    coeffs_list = []
    level = check_level(level)
    if level == 0:
        return [np.array(data)]
    a = data
    for i in range(level):
        a, d = dwt(a)
        coeffs_list.append(d)

    coeffs_list.append(a)
    coeffs_list.reverse()

    return coeffs_list


def inverseDwt(a, d):
    res = []
    for i in range(len(a)):
        x = (a[i] + d[i]) * np.sqrt(M) / 4
        y = (a[i] - d[i]) * np.sqrt(M) / 4
        res.extend([x, y])
    return np.array(res)


def waveReconstruct(coeffs):
    if len(coeffs) < 1:
        raise ValueError("Список коэффициентов слишком короткий (минимально 1).")
    elif len(coeffs) == 1:
        return coeffs[0]

    a, ds = coeffs[0], coeffs[1:]

    for d in ds:
        a = inverseDwt(a, d)

    return a
