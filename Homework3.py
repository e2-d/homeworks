import pandas as pd
import numpy as np


## 1. Привести различные способы создания объектов типа Series

index = ['a', 'b', 'c']

##списки Python или массивы NumPy

# np_ar = np.array(np.random.default_rng().integers(0, 9, 3))
# np_series = pd.Series(np_ar, index = index)
# print(np_series)

## - скалярные значение

# value = 42
# vel_series = pd.Series(value, index = index)
# print(vel_series)

## - словари

# dictionary = {'b' : 1, 'a' : 2, 'c' : 3}
# dict_series = pd.Series(dictionary, index = index)
# print(dict_series)

#-----------------------------------------------------------------------------
## 2. Привести различные способы создания объектов типа DataFrame
## - через объекты Series

# col_1 = np.array(np.random.default_rng().integers(0, 9, 3))
# col_2 = np.array(np.random.default_rng().integers(0, 9, 3))

# df_1 = pd.DataFrame([col_1, col_2], columns=['a', 'b', 'c'])
# print(df_1)


## - списки словарей

# dictionarys = [
#     {'Name': 'A', 'Age': 77},
#     {'Name': 'B', 'Age': 55},
#     {'Name': 'C', 'Age': 33}
# ]

# df_2 = pd.DataFrame(dictionarys)
# print(df_2)

## - словари объектов Series

# n_series = pd.Series(['A', 'B', 'C'])
# a_series = pd.Series([77, 55, 33])
# c_series = pd.Series(['M', 'S', 'B'])

# dictionary = {
#     'Name': n_series,
#     'Age': a_series,
#     'City': c_series
# }

# df_3 = pd.DataFrame(dictionary)
# print(df_3)

## - двумерный массив NumPy

# np_ar = np.arange(0,10).reshape(5,2)

# df_4 = pd.DataFrame(np_ar, columns=['group1', 'group2'])
# print(df_4)

## - структурированный массив Numpy

# dtype = [('Name', 'U10'), ('Age', 'i4')]

# data = [
#     ('A', 77),
#     ('B', 55),
#     ('C', 33)
# ]

# struc_array = np.array(data, dtype=dtype)

# df_5 = pd.DataFrame(struc_array)
# print(df_5)

#-------------------------------------------------------------------------------
## 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1

# population = pd.Series({
#     'city_1' : 1001,
#     'city_2' : 1002,
#     'city_3' : 1003,
#     'city_41' : 1004,
#     'city_51' : 1005
# })

# area = pd.Series({
#     'city_1' : 9991,
#     'city_2' : 9992,
#     'city_3' : 9993,
#     'city_42' : 9994,
#     'city_52' : 9995
# })

# data = pd.DataFrame({'area1' : area, 'pop1' : population}).fillna(1)
# print(data)

#-----------------------------------------------------------------------------------------------------------
## 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ

# rng = np.random.default_rng()

# A = rng.integers(0, 10, (3,4))

# df = pd.DataFrame(A, columns = ['a','b','c','d'])
# print(df)
# print('-------------------')

# print(df.iloc[::, 0])
# print('-------------------')
# print(df.sub(df.iloc[::, 0], axis = 0))

#-----------------------------------------------------------------------------------------------------------
## 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()

data = {
    'A': [np.nan, 2, 3, np.nan, 5],
    'B': [1, np.nan, 3, 4, np.nan],
    'C': [np.nan, 2, np.nan, 4, 5]
}

df = pd.DataFrame(data)

print(df)
print('---------------------------')
print(df.ffill(axis = 0))
print('---------------------------')
print(df.ffill(axis = 1))
print('\n', '-----------------------------------------------', '\n')
#------------------------------------------------

print(df)
print('---------------------------')
print(df.bfill(axis = 0))
print('---------------------------')
print(df.bfill(axis = 1))
