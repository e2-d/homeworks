import numpy as np
import pandas as pd

# # 2. 

# index = pd.MultiIndex.from_product(
#     [
#         ['city_1', 'city_2'],
#         [2010, 2020]
#     ],
#     names = ['city', 'year']
# )

# columns = pd.MultiIndex.from_product(
#     [
#         ['person_1', 'person_2', 'person_3'],
#         ['job_1', 'job_2']
#     ],
#     names = ['worker', 'job']
# )

# rng = np.random.default_rng(1)

# data = rng.random((4, 6))

# data_df = pd.DataFrame(data, index = index, columns = columns)
# print(data_df)
# print('-----------------------------------------------------------------------------------------------')

# # Из получившихся данных выбрать данные по 
# # - 2020 году (для всех столбцов)
# # - job_1 (для всех строк)
# # - для city_1 и job_2

# data_2020 = data_df.loc[(slice(None), 2020), :]
# print(data_2020)
# print('-----------------------------------------------------------------------------------------------')

# data_job_1 = data_df.loc[:, (slice(None), 'job_1')]
# print(data_job_1)
# print('-----------------------------------------------------------------------------------------------')

# data_city_1_job_2 = data_df.loc[('city_1', slice(None)), (slice(None), 'job_2')]
# print(data_city_1_job_2)

##---------------------------------------------------------------------------------------------------------------------------------------

# # 1. Разобраться как использовать мультииндексные ключи в данном примере
# index = [
#     ('city_1', 2010),
#     ('city_1', 2020),
#     ('city_2', 2010),
#     ('city_2', 2020),
#     ('city_3', 2010),
#     ('city_3', 2020),
# ]

# population = [
#     101,
#     201,
#     102,
#     202,
#     103,
#     203,
# ]
# pop = pd.Series(population, index = index)
# pop_df = pd.DataFrame(
#     {
#         'total': pop,
#         'something': [
#             10,
#             11,
#             12,
#             13,
#             14,
#             15,
#         ]
#     }
# )

# print(pop_df)
# print('-----------------------------------------------------------------------------------------------')

# # ???? ## pop_df_1 = pop_df.loc???['city_1', 'something']
# # ???? ## pop_df_1 = pop_df.loc???[['city_1', 'city_3'], ['total', 'something']]
# # ???? ## pop_df_1 = pop_df.loc???[['city_1', 'city_3'], 'something']

# pop_df_1 = pop_df.loc[[('city_1', 2010),('city_1', 2020)], 'something']
# print(pop_df_1)
# print('-----------------------------------------------------------------------------------------------')

# pop_df_2 = pop_df.loc[[('city_1', 2010),('city_1', 2020), ('city_3', 2010), ('city_3', 2020)], ['total', 'something']]
# print(pop_df_2)
# print('-----------------------------------------------------------------------------------------------')

# pop_df_3 = pop_df.loc[[('city_1', 2010),('city_1', 2020), ('city_3', 2010), ('city_3', 2020)], ['something']]
# print(pop_df_3)

#---------------------------------------------------------------------------------------------------------------------------------------

# # 3. Взять за основу DataFrame со следующей структурой
# index = pd.MultiIndex.from_product(
#     [
#         ['city_1', 'city_2'],
#         [2010, 2020]
#     ],
#     names=['city', 'year']
# )
# columns = pd.MultiIndex.from_product(
#     [
#         ['person_1', 'person_2', 'person_3'],
#         ['job_1', 'job_2']
#     ],
#     names=['worker', 'job']
# )

# rng = np.random.default_rng(1)

# data = rng.random((4, 6))

# data_df = pd.DataFrame(data, index = index, columns = columns)
# print(data_df)
# print('-----------------------------------------------------------------------------------------------')

# # Выполнить запрос на получение следующих данных
# # - все данные по person_1 и person_3
# # - все данные по первому городу и первым двум person-ам (с использование срезов)
# #
# # Приведите пример (самостоятельно) с использованием pd.IndexSlice

# df_person_1_person_3 = data_df.loc[:, ( ['person_1', 'person_3'] )]
# print(df_person_1_person_3)
# print('-----------------------------------------------------------------------------------------------')

# df_city_1_person_1_person_2 = data_df.loc[('city_1', slice(None)), ( ['person_1', 'person_2'] )]
# print(df_city_1_person_1_person_2)
# print('-----------------------------------------------------------------------------------------------')

# result_1 = data_df.loc[:, pd.IndexSlice['person_1':'person_3', :]]
# print(result_1)

#---------------------------------------------------------------------------------------------------------------------------------------

# #4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)
# ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
# ser2 = pd.Series(['c', 'f', 'b'], index=[3,4,5])

# print("ser1:")
# print(ser1)
# print("ser2:")
# print(ser2)
# print('-----------------------------------------------------------------------------------------------')

# result_outer = pd.concat([ser1, ser2], join='outer', axis=1)
# print("Outer join (join='outer'):")
# print(result_outer)
# print('-----------------------------------------------------------------------------------------------')

# result_inner = pd.concat([ser1, ser2], join='inner', axis=1)
# print("Inner join (join='inner'):")
# print(result_inner)
