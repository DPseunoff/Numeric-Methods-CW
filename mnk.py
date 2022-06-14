import numpy as np


def MNK_3(x, f):
    n = np.shape(x)[0]

    a = np.array([[n, np.sum(x), np.sum(x * x), np.sum(x * x * x)],
                  [np.sum(x), np.sum(x * x), np.sum(x * x * x), np.sum(x * x * x * x)],
                  [np.sum(x * x), np.sum(x * x * x), np.sum(x * x * x * x), np.sum(x * x * x * x * x)],
                  [np.sum(x * x * x), np.sum(x * x * x * x), np.sum(x * x * x * x * x), np.sum(x * x * x * x * x * x)]
                  ])
    b = np.array([[np.sum(f)], [np.sum(x * f)], [np.sum(x * x * f)], [np.sum(x * x * x * f)]])
    return get_SLAU_solve(LU(a), b)


def MNK_4(x, f):
    n = np.shape(x)[0]

    a = np.array([[n, np.sum(x), np.sum(x * x), np.sum(x * x * x), np.sum(x * x * x * x)],
                  [np.sum(x), np.sum(x * x), np.sum(x * x * x), np.sum(x * x * x * x), np.sum(x * x * x * x * x)],
                  [np.sum(x * x), np.sum(x * x * x), np.sum(x * x * x * x), np.sum(x * x * x * x * x), np.sum(x**6)],
                  [np.sum(x * x * x), np.sum(x * x * x * x), np.sum(x * x * x * x * x), np.sum(x**6), np.sum(x**7)],
                  [np.sum(x * x * x * x), np.sum(x * x * x * x * x), np.sum(x**6), np.sum(x**7), np.sum(x**8)]
                  ])
    b = np.array([[np.sum(f)],
                  [np.sum(x * f)],
                  [np.sum(x * x * f)],
                  [np.sum(x * x * x * f)],
                  [np.sum(x * x * x * x * f)]
                  ])
    return get_SLAU_solve(LU(a), b)


def get_SLAU_solve(a, b):
    n = a.shape[0]
    x = np.zeros(n)
    z = np.zeros(n)

    # Решение Lz = b
    def sum_lz(i):
        res = 0
        for j in range(i):
            res += a[i, j] * z[j]
        return res

    for i in range(n):
        z[i] = b[i] - sum_lz(i)

    # Решение Ux = z
    def sum_ux(i):
        res = 0
        for j in range(i, n):
            res += a[i, j] * x[j]
        return res

    for i in reversed(range(n)):
        x[i] = (z[i] - sum_ux(i)) / a[i, i]
    return x


def LU(a):
    n = a.shape[0]
    for i in range(n - 1):
        for j in range(i + 1, n):
            c = a[j][i] / a[i][i]
            a[j][i] = c
            for k in range(i + 1, n):
                a[j][k] = a[j][k] - a[i][k] * c
    return a
