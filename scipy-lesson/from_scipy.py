from scipy.optimize import minimize
import numpy as np

# Визначаємо функцію, що описує довжину огорожі


def fence_length(x):
    a, b = x
    return a + 2 * b


# Визначаємо обмеження
constraints = (
    {'type': 'eq', 'fun': lambda x: x[0] * x[1] - 1000},  # a * b = 1000
)

# Визначаємо межі для змінних
bounds = [(0, None), (0, None)]

# Початкові наближення для a та b
initial_guess = np.array([10, 100])

# Виконуємо мінімізацію
result = minimize(fence_length, initial_guess,
                  bounds=bounds, constraints=constraints)

if result.success:
    a, b = result.x
    print(f"Оптимальні розміри області: a = {a:.2f}, b = {b:.2f}")
    print(f"Мінімальна довжина огорожі: {fence_length(result.x):.2f} м")
else:
    print("Мінімізацію не вдалося виконати.")

    # -----------------------------------------------
# Зроблено за допомогою copilot, для додаткового прикладу вирішення