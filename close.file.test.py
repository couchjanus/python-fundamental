# -*- coding: utf-8 -*-
# close.file.test.py

my_file = open("README.md", "r")

print("Имя файла: ", my_file.name)

print("Файл закрыт: ", my_file.closed)

my_file.close()
print("А теперь закрыт: ", my_file.closed)
