import numpy as np
import pandas as pd

# pandas - расширение numpy (структурированные массивы). Строки и столбцы индексируются не только числами, но и метками

# основные структуры: Series, DataFrame, Index

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])

# print(data, type(data))

# print(data.values, data.index)

# print(type(data.values), type(data.index))

# print(data[0], data['a'])
# print(data[1:3], data['b':'d'])

# print(type(data.index))

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index = [1, 10, 7, 'd'])

# print(data[1])
# print(data[10:'d'])

# population_dict = {
#     'city_1' : 1001,
#     'city_2' : 1002,
#     'city_3' : 1003,
#     'city_4' : 1004,
#     'city_5' : 1005
# }

# population = pd.Series(population_dict)
# print(population)

# print(population['city_4'])
# print(population['city_4':'city_5'])

#Для создание Series можно использовать
# - списки python или массивы numpy
# - скалярные значение
# - словари

# 1. Привести различные способы создание объектов типа Series
#-------------------------------------------------------------------------------------------------------------------------------------------------
##DataFrame - двумерный массив с явно определенными индексами. Последовательность согласованных объектов типа Series

# population_dict = {
#     'city_1' : 1001,
#     'city_2' : 1002,
#     'city_3' : 1003,
#     'city_4' : 1004,
#     'city_5' : 1005
# }

# area_dict = {
#     'city_1' : 9991,
#     'city_2' : 9992,
#     'city_3' : 9993,
#     'city_4' : 9994,
#     'city_5' : 9995
# }

# population = pd.Series(population_dict)
# area = pd.Series(area_dict)

# states = pd.DataFrame({
#     'population1': population,
#     'area1': area
# })

# print(states)

# print(states.values, type(states.values))
# print(states.index, type(states.index))
# print(states.columns, type(states.columns))

# print(states['area1'])

#DataFrame. Способы создания
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив numpy
# - структурированный массив numpy

# 2. Привести различные способы создания объектов типа DataFrame
#----------------------------------------------------------------------------------------------------------------------------------------------
##Index - способ организации ссылки на данные объектов Series и DataFrame. Index - неизменяем и упорядочен, 
## явялется мультимножеством (могут быть повторяющиеся элементы)

# ind = pd.Index([2,3,5,7,11])
# print(ind[1])
# print(ind[::2])

#ind[1] = 5 - wrong

#Index следует соглашениям set(python)
# indA = pd.Index([1,2,3,4,5])
# indB = pd.Index([2,3,4,5,6])

# print(indA.intersection(indB))
#---------------------------------------------------------------------------
#выборка данных из Series
# data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])

# print('a' in data)
# print('z' in data)

# print(data.keys())

# data['a'] = 100
# print(data)

#как одномерный массив
# data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])

# print(data['a':'c'])
# print(data[0:2])
# print(data[(data > 0.5) & (data < 1)])
# print(data[['a', 'd']])

#атрибуты-индексаторы
# data = pd.Series([0.25, 0.5, 0.75, 1.0], index = [1, 3, 10, 15])

# print(data[1])

# print(data.loc[1])
# print(data.iloc[1])
#-------------------------------------------------------------------------------
#выборка данных из DataFrame
# population_dict = {
#     'city_1' : 1001,
#     'city_2' : 1002,
#     'city_3' : 1003,
#     'city_4' : 1004,
#     'city_5' : 1005
# }

# area_dict = {
#     'city_1' : 9991,
#     'city_2' : 9992,
#     'city_3' : 9993,
#     'city_4' : 9994,
#     'city_5' : 9995
# }

# population = pd.Series(population_dict)
# area = pd.Series(area_dict)

# data = pd.DataFrame({
#     'area1': area,
#     'population1' : population,
#     'population' : population
# })

# print(data['area1'])
# print(data.area1)

# print(data.population1 is data["population1"])
# print(data.population is data['population'])

# data['new'] = data['area1']

# data['new1'] = data['area1'] / data['population1']

# print(data)

#двумерный numpy-массив

# data = pd.DataFrame({
#     'area1': area,
#     'population1' : population,
#     'population' : population
# })

# print(data.T)

# print(data['area1'])

# print(data.values[0:3])

#атрибуты-индексаторы
#print(data.iloc[:3, 0:2])
# print(data.loc[:'city_4', 'population1':'population'])
#print(data.loc[data['population'] > 1002, ['area1', 'population1']])

# data.iloc[0, 2] = 999999

# rng = np.random.default_rng()
# s = pd.Series(rng.integers(0, 10, 4))

# print(s)
# print(np.exp(s))

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

# data = pd.DataFrame({'area1' : area, 'pop1' : population})

# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1
#---------------------------------------------------------------------------
# dfA = pd.DataFrame(rng.integers(0, 10, (2,2)), columns = ['a', 'b'])
# dfB = pd.DataFrame(rng.integers(0, 10, (3,3)), columns = ['a', 'b', 'c'])

# print(dfA, '-----------------', dfB)
# print('------------------')
# print(dfA + dfB)

# rng = np.random.default_rng()

# A = rng.integers(0, 10, (3,4))
# print(A)

# print(A[0])
# print(A - A[0])

# df = pd.DataFrame(A, columns = ['a','b','c','d'])
# print(df)

# print(df.iloc[0])
# print(df - df.iloc[0])

# print(df.iloc[0, ::2])
# print(df - df.iloc[0, ::2])

# 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ
#---------------------------------------------------------------------
#NaN = not a number

#NA - значения: NaN, null, -9999

#pandas. два способа хранения отсутствующих значений
#индикаторы NaN, None
#null

#None - объект. Не работает с sum, min

# vall = np.array([1, 4, np.nan, 1])
# print(vall.sum())
# print(np.sum(vall))
# print(np.nansum(vall))

# x = pd.Series(range(10), dtype = int)

# x[0] = None
# x[1] = np.nan

# print(x)

# x2 = pd.Series(['a', 'a', 'a'])

# x2[0] = None
# x2[1] = np.nan

# print(x2)

#

# x3 = pd.Series([1, 2, np.nan, None, pd.NA], dtype = 'Int32')

# print(x3)
# print(x3.isnull())
# print(x3[x3.isnull()])
# print(x3[x3.notnull()])
# print(x3.dropna())

# df = pd.DataFrame([
#     x,
#     x2,
#     x3
# ])

# print(df)
# print('---------------------------')
# print(df.dropna())
# print('---------------------------')
# print(df.dropna(axis = 0))
# print('---------------------------')
# print(df.dropna(axis = 1))

# how
# - all - все значения NA
# - any - хотя бы одно значение
# - thresh = x -остается, если остается минимум x непустых значения

# print(df.dropna(axis = 1, how = 'all'))
# print(df.dropna(axis = 1, how = 'any'))
# print(df.dropna(axis = 1,thresh = 2))