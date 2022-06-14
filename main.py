import pandas as pd
from scipy.stats import ttest_ind
pd.options.mode.chained_assignment = None

data = pd.read_csv("source/shmya_final_version.csv")

#Фильтруем данные для дальнейшей проверки гипотезы
more_than_two_cultery_data = data[data["cutlery"] > 2]
less_than_two_cultery_data = data[data["cutlery"] <= 2]

#Проверяем гипотезу
hypotez = ttest_ind(more_than_two_cultery_data["tips"], less_than_two_cultery_data["tips"])
print(hypotez)
#Значение p_value достаточно низкое, а статистика высока - это подтверждает правильность гипотезы

#Фильтруем значения в таблице
user_segment = more_than_two_cultery_data[more_than_two_cultery_data["order_price"] > 800]
user_segment["date"] = pd.to_datetime(user_segment["date"], format=f'%Y-%m-%d %H:%M:%S')
user_segment["date"] = user_segment["date"].dt.day.copy()
dates = (1,2,3,4,5,6,7,8)
user_segment = user_segment[~user_segment["date"].isin(dates)]

#Проверяем правильность введенных условий
print(f"Мин. сумма заказа: {user_segment['order_price'].min()}\n"
      f"Мин. день в месяце: {user_segment['date'].min()}\n"
      f"Мин. кол-во столовых приборов: {user_segment['cutlery'].min()}")

count_of_users = user_segment["uid"].count()
print(f"Колличество пользователей: {count_of_users}")
#Итого колличсетво пользователей - 3529

#Экспортируем полученную таблицу
result = user_segment["uid"]
result["index"] = result.index
result = result.reset_index(level=0)
result.to_csv("source/result.csv", encoding='utf-8', index=False, columns=["index", "uid"])