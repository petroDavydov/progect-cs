import numpy as np

# Складіть рівняння параболи,
# що проходить через задані три точки (1,12),(3,54), (-1,2)
# Необхідно знайти коефіцієнти рівняння
# a,b,cy = ax^2 + bx + c

# канонічне рівняння параболи:
# y^2 = 2px або y=2py
# формула за якою рахувати параболу:
# y=ax^2 + bx + c
# данні(x,y): (1,12),(3,54),(-1,2)

a_matrix = np.array([[1, 1, 1], [9, 3, 1], [1, -1, 1]])
print(f"This is a_matrix: \n", a_matrix)

b_matrix = np.array([12, 54, 2])
print(f"This is b_matrix: \n", b_matrix)

result = np.linalg.solve(a_matrix, b_matrix)
print(f"This is result: \n", result)
