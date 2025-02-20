import sympy as sp

print("Математичний аналіз\n")

x = sp.symbols('x')
expr = x**3 + 2*x**2 + x
derivative = sp.diff(expr, x)
print("Use 'diff': \n", derivative, "\n")
# ---------------------------------------

print("Для похідних вищого порядку необхідно додати аргумент до функції diff: \n")

second_derivative = sp.diff(expr, x, 2)
print("Add argument to 'diff': \n", second_derivative, "\n")
# ---------------------------------------
print("Інтегрування – це процес знаходження первісної функції\n")

expr = x**3 + 2*x**2 + x
integral = sp.integrate(expr, x)
print("Use 'integrate': \n", integral, "\n")
# ---------------------------------------
print("Для знаходження визначеного інтегралу необхідно додати межі інтегрування\n")

defined_integral = sp.integrate(expr, (x, 0, 1))
print("Add integration limits:\n", defined_integral, "\n")
# ---------------------------------------
print("Для знаходження границі функції використовується функція limit:\n")

limit_expr = sp.limit(sp.sin(x)/x, x, 0)
print("Use 'limit': \n", limit_expr, "\n")
# ---------------------------------------
