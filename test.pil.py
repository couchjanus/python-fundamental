# -*- coding: utf-8 -*-
# test.pil.py

from __future__ import print_function

from PIL import Image

f = open("cat1.jpg", "rb") # Открываем файл в бинарном режиме
img = Image.open(f)        # Передаем объект файла

# Получаем размер изображения
print("original =", img.mode, img.size)

img.draft("L", (100, 100))
print("draft =", img.mode, img.size)

f.close()                  # Закрываем файл
