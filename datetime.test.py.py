# -*- coding: utf-8 -*-
# datetime.test.py

import datetime

# создать простой объект даты. 

print(datetime.date(2019, 12, 14)) # 2019-12-14

# print(datetime.date(2019, 13, 14))

d = datetime.date(2020, 12, 14)

print(d.year) # 2020
print(d.day)  # 14
print(d.month) # 12


# посмотрим, какой сейчас день:

print(datetime.date.today()) # 

# Это может быть полезно, когда вам нужно записать, какой сейчас день. 
# Или, если вам нужно выполнить основанный на сегодняшней дате расчет. 

a = datetime.datetime(2019, 3, 5)
print(a) # 

b = datetime.datetime(2019, 3, 5, 12, 30, 10)
print(b) # 

d = datetime.datetime(2019, 3, 5, 12, 30, 10)
print(d.year) # 2019
print(d.second) # 10
print(d.hour) # 12


# today совместно с datetime.datetime использует два разных метода:

a = datetime.datetime.today()
print(a) # 

b = datetime.datetime.now()
print(b) # 


# Пример, как конвертировать сегодняшний объект datetime в строку, следующую за форматом YYYYMMDD (ГГГГММДД).

a = datetime.datetime.today().strftime("%Y%m%d")
print(a) #

# присваиваем объект datetime переменной под названием today и применяем два разных параметра форматирования строки. 
# Первый параметр добавляет косые черточки между элементами datetime, а также перегруппировывает datetime, теперь он делится на месяц, день и год. 

today = datetime.datetime.today()
print( today.strftime("%m/%d/%Y") ) #

# создаем временную отметку, которая следует типичному формату: YYYY-MM-DD.HH.MM.SS. 
# Если вам нужно указать год как двухзначный (“YY”), вы можете заменить %Y на %y.
print( today.strftime("%Y-%m-%d-%H.%M.%S") ) # 
