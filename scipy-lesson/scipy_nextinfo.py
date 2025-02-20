import scipy.constants as pc
from scipy.optimize import minimize
from scipy.interpolate import griddata
from scipy.interpolate import LinearNDInterpolator
from mpl_toolkits.mplot3d import axes3d
from scipy.interpolate import interp2d
from scipy.interpolate import interp1d
from scipy.integrate import solve_ivp
from scipy import integrate
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import constants
# # ---------------------------------
# cnst = constants
# # ---------------------------------

# print(cnst.Stefan_Boltzmann)

# print(f"Найпростіший приклад - це обчислення площі фігури за допомогою інтегралу.")
# result = integrate.quad(lambda x: np.sin(x), 0, np.pi)
# print("This is area of the figure: \n", result)
# # -------------------------------------------

# # result = integrate.quad(lambda x: 1/x, 1, np.inf)
# # print("Наприклад, для функції f(x)=1/x інтеграл розходиться і ми отримаємо результат: \n", result)

# # ----------------------------------------------

# result = integrate.quad(lambda x: 1/(x**2), 1, np.inf)
# print("для функції f(x)=1/x**2 інтеграл сходиться і ми отримуємо кінцевий результат: \n", result)
# # ----------------------------------------------

# result = integrate.quad(lambda x: np.sin(x)/x, -1, 1, points=[0])
# print("""Якщо потрібно інтегрувати функцію з точками розриву,
# необхідно передавати точки розриву в спеціальному параметрі
# списку points: \n""", result)
# # ------------------------------------------------


# def func(x, a):
#     f = (np.exp(x / a) + np.exp(-x / a)) ** 2
#     return np.pi * f


# result = integrate.quad(func, 0, 5, args=(3,))
# print("Обчислимо об'єм тіла обертання. \n", result)
# # ------------------------------------------------

# # From course
# # f = lambda y, x: x**2 + y**2
# # a, b = 0, 1
# # gfun = lambda x: 0
# # hfun = lambda x: x**2

# # result = integrate.dblquad(f, a, b, gfun, hfun)

# # print("Обчислимо двократний інтеграл: \n", result)
# # ------------------------------------------------

# # When save (ctrl + s)


# def f(y, x): return x**2 + y**2


# a, b = 0, 1
# def gfun(x): return 0
# def hfun(x): return x**2


# result = integrate.dblquad(f, a, b, gfun, hfun)

# print(result)
# print("Обчислимо двократний інтеграл: \n", result)
# # ------------------------------------------------
# print("""Диференціальне рівняння:
# scipy.integrate.solve_ivp
# ("solve an initial value problem")\n""")

# k = 0.5
# N = 1000
# y0 = 10
# t0, tf = 0, 25


# def dydt(t, y):
#     return k * y * (1 - y / N)


# soln = solve_ivp(dydt, (t0, tf), [y0])
# print("Нам необхідно визначити функцію,маємо наступне повідомленн: \n", soln)
# # -------------------------------------------------

# # soln = solve_ivp(dydt, (t0, tf), [y0])
# t, y = soln.t, soln.y[0]
# plt.plot(t, y, 'o', color='k', label='solve_ivp')
# plt.legend()
# plt.show()
# # --------------------------------------------------

# soln = solve_ivp(dydt, (t0, tf), [y0], dense_output=True)
# t, y = soln.t, soln.y[0]
# z, = soln.sol(t)
# plt.plot(t, y, 'o', color='k', label='solve_ivp')
# plt.plot(t, z, color='blue', label='Interpolation')
# plt.legend()
# plt.show()
# # ------------------------------------------------

# print("Інтерполяція функцій \n")

# print("""Функціональність найпростішої та очевидної
# одновимірної інтерполяції надає метод
# scipy.interpolate.interp1d.\n""")
# print("""Інтерполяція — спосіб знаходження проміжних значень
# величини за наявного дискретного набору відомих значень.\n""")

# date = np.linspace(1, 8, 8)
# day = [23, 17, 17, 16, 15, 14, 17, 20]
# print("kind='linear' \n")
# f = interp1d(date, day, kind='linear')

# plt.plot(date, day, 'o')
# more_date = np.linspace(1, 8, 100)
# plt.plot(more_date, f(more_date))
# plt.ylim(0, 25)
# plt.title("kind='linear' \n")
# plt.show()
# # -------------------------------
# print("kind='nearest' \n")
# f = interp1d(date, day, kind='nearest')

# plt.plot(date, day, 'o')
# more_date = np.linspace(1, 8, 100)
# plt.plot(more_date, f(more_date))
# plt.ylim(0, 25)
# plt.title("kind='nearest' \n")
# plt.show()
# # ----------------------------------
# print(" kind='cubic'")
# f = interp1d(date, day, kind='cubic')

# plt.plot(date, day, 'o')
# more_date = np.linspace(1, 8, 100)
# plt.plot(more_date, f(more_date))
# plt.ylim(0, 25)
# plt.title(" kind='cubic' \n")
# plt.show()
# # -----------------------------------

# print("kind='quadratic' \n")
# x = [1, -1, 3]
# y = [2, 2, 54]
# f = interp1d(x, y, kind='quadratic')
# plt.plot(x, y, 'o')
# more_x = np.linspace(-1, 3, 100)
# plt.plot(more_x, f(more_x))
# plt.title("kind='quadratic'")
# plt.show()
# # ----------------------------------

# print("Багатовимірна інтерполяція \n")
# print("""Для двовимірної інтерполяції
# використовується метод scipy.interpolation.interp2d. \n""")


# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)
# z = np.linspace(0, 100, 100)

# X, Y = np.meshgrid(x, y)

# px, py, pz = np.random.choice(x, 50), np.random.choice(
#     y, 50), np.random.choice(z, 50)

# # f = interp2d(px, py, pz, kind='cubic')  # removed from Scipy 1.14.0
# f = LinearNDInterpolator(list(zip(px, py)), pz)

# Z = f(X, Y)

# fig = plt.figure()
# ax = fig.add_subplot(projection="3d")
# ax.plot_surface(X, Y, Z)

# plt.show()
# # ----------------------------------------

# x = np.linspace(-10, 10, 1000)
# y = np.linspace(-10, 10, 1000)
# X, Y = np.meshgrid(x, y)


# def f(x, y):
#     return x ** 2 * y ** 2 + 2


# px, py = np.random.choice(x, 250), np.random.choice(y, 250)

# z = griddata((px, py), f(px, py), (X, Y), method='cubic')

# fig = plt.figure()
# ax = fig.add_subplot(projection="3d")
# ax.plot_surface(X, Y, z)

# plt.show()
# # -------------------------------------------
# print("Мінімізація без обмежень")


# x = np.linspace(-10, 10, 10000)
# y = np.linspace(-10, 10, 10000)
# X, Y = np.meshgrid(x, y)

# px, py = np.random.choice(x, 2500), np.random.choice(y, 2500)


# def paraboloid(arg):
#     x, y = arg
#     return x ** 2 + y ** 2


# z = griddata((px, py), paraboloid((px, py)), (X, Y), method='cubic')
# plt.contour(x, y, z)
# plt.show()
# # -------------------------------------------------------------

# x = np.linspace(-10, 10, 10000)
# y = np.linspace(-10, 10, 10000)
# X, Y = np.meshgrid(x, y)

# px, py = np.random.choice(x, 2500), np.random.choice(y, 2500)


# def f(arg):
#     x, y = arg
#     return x ** 2 * y ** 2 + 2


# z = griddata((px, py), f((px, py)), (X, Y), method='cubic')
# plt.contour(x, y, z)
# plt.show()
# # ---------------------------------------------------------

# x = np.linspace(-10, 10, 10000)
# y = np.linspace(-10, 10, 10000)
# X, Y = np.meshgrid(x, y)

# px, py = np.random.choice(x, 2500), np.random.choice(y, 2500)


# def f(arg):
#     x, y = arg
#     return x ** 2 * y ** 2 + 2


# z = griddata((px, py), f((px, py)), (X, Y), method='cubic')

# plt.contour(x, y, z)
# plt.show()
# # ------------------------------------------------------------

print("мінімізація з обмеженнями \n")


def paraboloid(arg):
    x, y = arg
    return x ** 2 + y ** 2


xbounds = (1, None)
ybounds = (1, None)
bounds = (xbounds, ybounds)
result = minimize(paraboloid, [1, 5], bounds=bounds, method='slsqp')

print(result)
# --------------------------------------------------


alpha = np.pi / 4  # кут запуску в радіанах (45 градусів)
speed = 35  # початкова швидкість
# Створюється масив 𝑥  з 1000 рівномірно розподілених значень від 0 до 120
x = np.linspace(0, 120, 1000)
# Обчислюється вертикальна координата 𝑦  для кожного значення 𝑥 за формулою
y = x * np.tan(alpha) - (pc.g * x**2)/(2 * speed**2 * np.cos(alpha) ** 2)

plt.grid()
plt.plot(x, y)
plt.show()
# ---------------------------------------------
