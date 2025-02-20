import sympy as sp
# --------------------------------------
print("Для розв'язування лінійних рівнянь використовується функція solve: \n")

x = sp.symbols('x')  # визначили сивол для рботи з ним

equation = sp.Eq(2*x + 1, 0)
solution = sp.solve(equation, x)

print("Use solve with method Eq: \n", solution, "\n")
# ---------------------------------------
print("Квадратні рівняння: \n")

equation = sp.Eq(x**2 + 5*x + 6, 0)
solution = sp.solve(equation, x)
print("Квадратне рівняння, use Eq & solve: \n", solution)
# ---------------------------------------
print("Більш складні нелінійні рівняння: sin(x)−x/2=0. \n")

equation = sp.Eq(sp.sin(x) - x/2, 0)
solution = sp.nsolve(equation, x, 1)
print("Нелінійні рівняння, use nsolve: \n", solution, "\n")
# ---------------------------------------
print("Розв'язувати системи лінійних рівнянь \n")

x, y = sp.symbols('x y')
equation1 = sp.Eq(2*x + y, 1)
equation2 = sp.Eq(x - y, 2)
solution = sp.solve((equation1, equation2), (x, y))
print("Системи лінійних рівнянь: \n", solution, "\n")
# ---------------------------------------
print("Для факторизації поліномів використовується функція factor: \n")

polynomial = x**3 - 3*x**2 + 3*x - 1
factored = sp.factor(polynomial)
print("Polynomial use 'factor': \n", factored, "\n")
# ---------------------------------------
print("Для розкладання полінома на множники використовується функція apart: \n")

rational_expr = (x**2 + 2*x + 1) / (x**2 + x)
apart_expr = sp.apart(rational_expr)
print("Use 'apart': \n", apart_expr, "\n")
# ---------------------------------------
print("Для знаходження коренів полінома використовується функція roots:\n")

polynomial = x**3 - 6*x**2 + 11*x - 6
roots = sp.roots(polynomial, x)
print("Use 'roots': \n", roots, "\n")
# ---------------------------------------
