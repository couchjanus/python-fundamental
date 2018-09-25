# -*- coding: utf-8 -*-
# oop.file.object.class.test.py

from os.path import join

class FileObject:
    '''Обёртка для файлового объекта, чтобы быть уверенным в том, что файл будет закрыт при удалении.'''
    def __init__(self, filepath='~', filename='sample.txt'):
        # открыть файл filename в filepath в режиме чтения и записи
        self.file = open(join(filepath, filename), 'r+')
    def __del__(self):
        self.file.close()
        del self.file