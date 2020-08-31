import numpy as np

# Задание 1
a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])
print(a)
print("-"*10)

one = (a[0, 0], a[1, 0], a[2, 0], a[3, 0], a[4, 0])
mean_one = np.mean(one)

two = (a[0, 1], a[1, 1], a[2, 1], a[3, 1], a[4, 1])
mean_two = np.mean(two)

mean_a = np.array([mean_one, mean_two])
print(mean_a)
print("-"*10)


# Задание 2
a_centered = np.subtract(a, mean_a)
print(a_centered)
print("-"*10)

# Задание 3

scal_one = a_centered[0:5, 0]
scal_two = a_centered[0:5, 1]
print(scal_one)
print(scal_two)

a_centered_sp = scal_one @ scal_two
print(a_centered_sp)






