# concat.sequence.test.py

a = [3, 2, 1]
b = [4, 5, 6]

a + b  # [3, 2, 1, 4, 5, 6]

print('a: ',  a)
print('b: ',  b)
print('a+b:  ', (a+b))

# Создать список L
L=[3,1,5,'a','b','cd',2.5,5.5,7.5] 
print(L)

L1 = L[:] # создание второй копии списка. Здесь создается вторая копия обьекта.

print(L + L1)

print(L1 * 3)