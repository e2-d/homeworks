import numpy as np
import sys
import array as arr

#------- Задания №1, 2 ---------
a1 = arr.array('i', [-1,2,3])
print(sys.getsizeof(a1))
print(type(a1))

# В Python сущестувет несколько кодов типов. Приведу пример нескольких из них: arr.array('u',['a','b','c']),
#  arr.array('L', [1,2,3]), arr.array('d', [1.1111111,2.2222222,3.3333333])

a2 = arr.array('d', [1.1111111,2.2222222,3.3333333])
print(sys.getsizeof(a2))
print(type(a2))


#------- Задания №3-6 ---------
# print(np.linspace(0, 1, 5))

# print(np.random.rand(5))

# print(np.random.normal(loc=0, scale=1, size=5))

# print(np.random.randint(0, 10, size=5))


#------- Задания №7 ---------
# matrix = np.arange(12).reshape(3, 4)

# print(matrix)
# print('-------')

# print(matrix[:2, :3])
# print('-------')

# print(matrix[:, 1])
# print('-------')

# print(matrix[::-1, ::-1])
# print('-------')

# print(matrix[:, 1])
# print('-------')

# print(matrix[2, :])
# print('-------')


#------- Задания №8 ---------
# original_list = np.arange(3)
# sliced_copy = original_list[0].copy()

# sliced_copy = 100
# print(original_list, '-------', sliced_copy)


#------- Задания №9 ---------
# vector = np.arange(3)

# row_vector = vector[np.newaxis, :]
# col_vector = vector[:, np.newaxis]

# print(vector)
# print('--------')
# print(row_vector)
# print('--------')
# print(col_vector)


#------- Задания №12 ---------
# a = np.arange(1, 4)
# b = np.arange(4, 7)

# result = np.dstack((a, b))

# print(a.ndim, b.ndim, result.ndim)
# print(np.dstack((a, b)))

# c = np.stack((a, b))

# print(c)
# print('--------')
# print(np.split(c, 2, axis=0))
# print(np.vsplit(c, 2))
# print('--------')
# print(np.split(c, 3, axis=1))
# print(np.hsplit(c, 3))

# r = np.arange(8).reshape(2, 2, 2)

# print(r)
# print('--------')
# print(np.dsplit(r, 2))