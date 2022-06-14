import matplotlib.pyplot as plt
import numpy as np

from functions import *
from wavevlet_methods import *
import mnk as mnk


def graphics(x, y, wX, coeffs, level):

    # a3, b3, c3, d3 = mnk.MNK_3(x, y)
    # mnkY = [float(a3 + b3 * xk + c3 * xk * xk + d3 * xk * xk * xk) for xk in x]

    a4, b4, c4, d4, e4 = mnk.MNK_4(x, y)
    mnkY = [float(a4 + b4 * xk + c4 * xk * xk + d4 * xk * xk * xk + e4 * xk * xk * xk * xk) for xk in x]

    cA = 'cA, Level-{0}'.format(level)
    cD = 'cD, Level-{0}'.format(level)

    label1 = 'Рис. 3.1. Исходный сигнал'
    label2 = 'Рис. 3.2. МНК 3-ей степени'
    label3 = 'Рис. 3.7. Коэффициенты апроксимации. Уровень {0}'.format(level)
    label4 = 'Рис. 3.8. Коэффициенты детализации. Уровень {0}'.format(level)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    # ax1 = plt.subplot(411)
    ax1.plot(x, y, color='black')
    # ax1.set_title('Исходный сигнал')
    ax1.set_xlabel(label1)
    ax1.grid()

    ax2.plot(x, mnkY, color='green', label="Level-3")
    ax2.legend(loc=1)
    # ax3.set_title('Апроксимация МНК')
    ax2.set_xlabel(label2)
    ax2.grid()
    # ax2 = plt.subplot(412)
    ax3.plot(wX, coeffs[0], color='blue', label=cA)
    ax3.legend(loc=1)
    ax3.set_xlabel(label3)

    # ax2.set_title('Коэффициенты аппроксимации')
    ax3.grid()
    # ax3 = plt.subplot(421)
    ax4.plot(wX, coeffs[1], color='red', label=cD)
    ax4.legend(loc=1)
    # ax4.set_title('Коэффициенты детализации')
    ax4.set_xlabel(label4)

    ax4.grid()
    # ax4 = plt.subplot(422)
    plt.show()


def f1_analysis(level):
    level = check_level(level)
    X = np.arange(0, 16, 0.1)
    y = [f1(x) for x in X]
    coeffs = waveDecompose(y, level)
    wX = np.arange(0, 16 / (2 ** level), 0.1)
    graphics(X, y, wX, coeffs, level)


def f2_analysis(level):
    level = check_level(level)
    X = np.arange(0, 128, 0.1)
    y = [f2(x) for x in X]
    coeffs = waveDecompose(y, level)
    wX = np.arange(0, 128 / (2 ** level), 0.1)
    graphics(X, y, wX, coeffs, level)


def f3_analysis(level):
    level = check_level(level)
    X = np.arange(0, 16, 0.1)
    y = [f3(x) for x in X]
    coeffs = waveDecompose(y, level)
    wX = np.arange(0, 16 / (2 ** level), 0.1)
    graphics(X, y, wX, coeffs, level)


def inverse():
    signal = [1, 2, 3, 4, 5, 6, 7, 8]
    print('Входной сигнал:', signal)
    coeffs = waveDecompose(signal, 1)
    print('\nКоэффициенты на 1-ом уровне:')
    print('А: ', coeffs[0])
    print('Д: ', coeffs[1])
    returned_signal = waveReconstruct(coeffs)
    print('Сигнал через коэффициенты: ', returned_signal)

    coeffs = waveDecompose(signal, 2)
    print('\nКоэффициенты на 2-ом уровне:')
    print('А: ', coeffs[0])
    print('Д: ', coeffs[1])
    returned_signal = waveReconstruct(coeffs)
    print('Сигнал через коэффициенты: ', returned_signal)

    coeffs = waveDecompose(signal, 3)
    print('\nКоэффициенты на 3-ом уровне:')
    print('А: ', coeffs[0])
    print('Д: ', coeffs[1])
    returned_signal = waveReconstruct(coeffs)
    print('Сигнал через коэффициенты: ', returned_signal)
    print()


def main():
    while True:
        print("1 - Сигнал со стационарно частотным спектром")
        print("2 - Сигнал с нестационарным частотным спектром")
        print("3 - Сигнал с динамическим частотным спектром")
        print("4 - Обратное ДВП")
        print("5 - Выход")
        m = int(input("Введите номер исследуемого сигнала (функции): "))

        if m < 1 or m > 5:
            print("Неверно введенный номер")
            continue
        if m == 5:
            print('Работа завершена')
            break
        if m == 1:
            level = int(input('Введите уровень преобразования: '))
            f1_analysis(level)
            continue
        if m == 2:
            level = int(input('Введите уровень преобразования: '))
            f2_analysis(level)
            continue

        if m == 3:
            level = int(input('Введите уровень преобразования: '))
            f3_analysis(level)
            continue

        if m == 4:
            inverse()
            continue


main()
