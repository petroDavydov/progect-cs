import sympy as sp

x = sp.symbols('x')
y = sp.symbols('y')

exp1 = x + 2*y
exp2 = x**2 + 3*x + 2
exp3 = exp1 + exp2
exp4 = exp1 * exp2
simplified_expr = sp.simplify((x**2 + 2*x + 3)/x)
expand_expr = sp.expand(exp4)
expand_expr1 = sp.expand(exp3)

print("This is x: \n", x)
print("This is y: \n", y)
print("This is exp1: \n", exp1)
print("This is exp2: \n", exp2)
print("This is exp3: \n", exp3)
print("This is exp4: \n", exp4)
print("""Спрощення складних алгебраїчних виразів.
Для цього використовується функція simplify \n""", simplified_expr)
print("Розкриття дужок. Для цього використовується функція expand: \n",
      expand_expr, "\n", "Next: \n", expand_expr1)
