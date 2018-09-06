# -*- coding: utf-8 -*-
# def.test.py

def print_yes():
    print('yes')

print_yes()  # yes

print_yes_alias = print_yes

print_yes_alias()  # yes

def mutate_list(a_list):
    a_list.append(0)
    return True


my_list = [1]
print(my_list)  # [1]

mutate_list(my_list)  # True
print(my_list)  # [1, 0]

