import numpy as np

#Задание №1
a = np.ones((3,2))
b = np.arange(3).reshape(-1,1)

print(a+b)

#Задание №2
y = np.array([[1,2,3,4,5], [6,7,8,9,10]])

mask = (y > 3) & (y < 9)
print(np.count_nonzero(mask))
print(np.count_nonzero(mask, axis = 0))
print(np.count_nonzero(mask, axis = 1))

#Вар. 2
# print(np.sum((y > 3) & (y < 9)))
# print(np.sum((y > 3) & (y < 9), axis = 0))
# print(np.sum((y > 3) & (y < 9), axis = 1)) 