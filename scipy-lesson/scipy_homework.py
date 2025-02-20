from scipy.optimize import minimize
from scipy import integrate
from scipy.interpolate import interp1d, interp2d, griddata
import numpy as np
import matplotlib.pyplot as plt


speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]
count = len(speed)
print("This is function count: \n", count)

length_speed = len(speed) - 1
time = np.linspace(0, length_speed, length_speed + 1)

print("This is time , use len(speed): \n", time)
# --------------------------------------------

plt.scatter(time, speed, marker='o')
plt.ylim(0, 130)
plt.xlim(0, length_speed)
plt.grid()
plt.show()
# --------------------------------------------


f_cubic = interp1d(time, speed, kind='cubic')
continuos_time = np.linspace(0, length_speed, 10000)
plt.ylim(0, 130)
plt.xlim(0, length_speed)
plt.grid()
plt.plot(continuos_time, f_cubic(continuos_time))
plt.show()
# ------------------------------------

result_cubic, _ = integrate.quad(f_cubic, 0, length_speed)
print("This is result_cubic: \n", result_cubic)
# -------------------------------------

f_quadratic = interp1d(time, speed, kind='quadratic')
plt.ylim(0, 130)
plt.xlim(0, length_speed)
plt.grid()
plt.plot(continuos_time, f_quadratic(continuos_time))
plt.show()
# ----------------------------------------------------

result_quadratic, _ = integrate.quad(f_quadratic, 0, length_speed)
print("This is result_quadratic : \n", result_quadratic)
print("This is result_quadratic, : \n", result_quadratic,)
print("This is result_quadratic, _ : \n", result_quadratic, _)
# ----------------------------------------------------------


# objective function: calculates the length of the fence without one side
def area(args):
    x, y = args
    return x + 2*y


# the area must be equal to 1000
constraints = ({'type': 'eq', 'fun': lambda args:  args[0] * args[1] - 1000})

xbounds = (0, 1000)
ybounds = (0, 1000)
bounds = (xbounds, ybounds)

result = minimize(area, [1, 999], bounds=bounds, constraints=constraints)
print("Homework 2, result: \n",result)
# ----------------------------------------------