import numpy as np

#Вкладник поклав 50000 умовних одиниць на три різні рахунки в три різні банки.
#За першим рахунком виплати становитимуть 5% річних,
# по другому – 7% річних та по третьому 6% річних.
# Відомо, що через рік вкладник отримав за відсотками
# суму в 2250 у.о. з першого та другого банку
# та суму в 1400 у.о. з першого та третього банку.
# Скільки умовних одиниць він поклав на кожен рахунок спочатку?

first_line = [1,1,1]
second_line = [0.05, 0.07, 0]
third_line = [0.05, 0, 0.06]
equal_line = [50000, 2250, 1400]

print(f"Print first_line: \n", first_line)
print(f"Print second_line: \n", second_line)
print(f"This is third_line: \n", third_line)
print(f"Print equal_line: \n", equal_line)

matrix_A = np.array([first_line,second_line,third_line])
print(f"This is matrix_A: \n", matrix_A)

matrix_B = np.array(equal_line)
print(f"This is equal_line: \n", equal_line)

result= np.linalg.solve(matrix_A, matrix_B)
print(result)

# ---

#answer - [10000. 25000. 15000.]