from scipy import integrate
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import constants
# ---------------------------------
cnst = constants
# ---------------------------------

# print(cnst.Stefan_Boltzmann)

print(f"Найпростіший приклад - це обчислення площі фігури за допомогою інтегралу.")
result = integrate.quad(lambda x: np.sin(x), 0, np.pi)
print("This is area of the figure: \n", result)
# -------------------------------------------

# result = integrate.quad(lambda x: 1/x, 1, np.inf)
# print("Наприклад, для функції f(x)=1/x інтеграл розходиться і ми отримаємо результат: \n", result)

# ----------------------------------------------

result = integrate.quad(lambda x: 1/(x**2), 1, np.inf)
print("для функції f(x)=1/x**2 інтеграл сходиться і ми отримуємо кінцевий результат: \n", result)
# ----------------------------------------------

result = integrate.quad(lambda x: np.sin(x)/x, -1, 1, points=[0])
print("""Якщо потрібно інтегрувати функцію з точками розриву,
необхідно передавати точки розриву в спеціальному параметрі
списку points: \n""", result)
# ------------------------------------------------


def func(x, a):
    f = (np.exp(x / a) + np.exp(-x / a)) ** 2
    return np.pi * f


result = integrate.quad(func, 0, 5, args=(3,))
print("Обчислимо об'єм тіла обертання. \n", result)
# ------------------------------------------------

# From course
# f = lambda y, x: x**2 + y**2
# a, b = 0, 1
# gfun = lambda x: 0
# hfun = lambda x: x**2

# result = integrate.dblquad(f, a, b, gfun, hfun)

# print("Обчислимо двократний інтеграл: \n", result)
# ------------------------------------------------

# When save (ctrl + s)


def f(y, x): return x**2 + y**2


a, b = 0, 1
def gfun(x): return 0
def hfun(x): return x**2


result = integrate.dblquad(f, a, b, gfun, hfun)

print(result)
print("Обчислимо двократний інтеграл: \n", result)
# ------------------------------------------------
