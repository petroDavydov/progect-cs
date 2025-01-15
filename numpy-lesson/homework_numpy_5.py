import numpy as np

# Складіть функцію get_polynom, яка за набором точок виду
# яка за набором точок виду (x1,y1),(x2,y2),.....(xn + yn + 1)
# буде знаходити коефіціент багаточлена ci.
# Таким чином функція приймає список картежів з координатами
# та повертає набір коефіцієнтів c0, c1,...,cn


def get_polynom(coords):

    x = np.array([coord[0] for coord in coords])
    print(f"This is x: \n", x)
    y = np.array([coord[1] for coord in coords])
    print(f"This is y: \n", y)
    # ---
    a_matrix = np.vander(x, len(x), increasing=True)
    print(f"This is a_matrix: \n", a_matrix)
    b_matrix = y
    print(f"This is b_matrix: \n", b_matrix)
    # ---
    return np.linalg.solve(a_matrix, b_matrix)


print(f"This is get_polynome answer: \n",
      get_polynom([(1, 12), (3, 54), (-1, 2)]))

# vander:
# https://numpy.org/doc/stable/reference/generated/numpy.vander.html#numpy-vander
