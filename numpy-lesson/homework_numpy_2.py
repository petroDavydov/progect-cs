import numpy as np

# На складі зберігаються мобільні телефони iPhone 12 (x), iPhone 13(y), iPhone 15(z) моделей.
# Всього 1328 екземплярів.
# Моделей iPhone 12 на 120 менше, ніж моделей iPhone 13(було 12 виправив на 13),
# та на 100 більше, ніж моделей iPhone 15.
# Скільки моделей кожного виду на складі?

# x+y+z =1328
# y - x = 120 або x=y−120
# x - z = 100 або x=z+100
# x - ?
# y - ?
# z - ?

A_full_array = np.array([[1, 1, 1], [-1, 1, 0], [1, 0, -1]])
print(f"This is A_full_array: \n", A_full_array)

B_equel_array = np.array([1328, 120, 100])
print(f"This is B_equel_array: \n", B_equel_array)

result=np.linalg.solve(A_full_array, B_equel_array)
print(f"This is result: \n", result)

#This is result: [436. 556. 336.]