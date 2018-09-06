# -*- coding: utf-8 -*-
# tuple.test.py

t = 1,[2,3]
print(t)

p = (1.2, 3.4, 0.9)
one_item = (1, )
empty_tuple = ()
my_tuple = 1, 'some', 3.5  # то же, что и (1, 'some', 3.5)
my_tuple = 'a',  # то же, что и ('a',)

p1 = 1, 3, 9
p2 = 3, 8, 5, # тоже три элемента


# t[1] = 2

t[1].append(4)
print(t)

tuple('abc')

print(tuple('abc'))


tuple() # ()
tuple('abc')  # ('a', 'b', 'c')
tuple([1, 2, 3])  # (1, 2, 3)

a,b='c','d' 
print(a,b)

a,b,c='ijk' 
print(a,b,c)

[A,B]=(1,2)
print(A,B)

a,b,c=range(3)
print(a,b,c)

a,b=1,2
print(a,b)

# код действительно проще и изящнее:
a, b = b, a

print(a,b)

a=b=c=1

c=1; b=c; a=b

a=b=c=[]
a.append(1)
print(a,b,c)

a = ()
b = ()
a is b # True
id(a) == id(b)  # True


tuple_0 = (1, 2, 3)

print('tuple_0 %s' % id(tuple_0))  # 140332152236648

tuple_1 = (1, 2, 3)

print('tuple_1 %s' % id(tuple_1))  # 140332152236720
del tuple_1

# Далее предполагается, что сборка мусора уже прошла.
# Проще всего наблюдать за работой из интерактивного сеанса
# интерпретатора.

tuple_2 = (1, 2, 4)

print('tuple_2 %s' % id(tuple_2))  # 140332152236720
