#begin24. Даны переменные A, B, C. 
#Изменить их значения, переместив содержимое A в C, C — в B, B — в A, и вывести новые значения переменных A, B, C.
a = float(input())
b = float(input())
c = float(input())
t = a
a = c
c = b 
b = t
print(a)
print(b)
print(c)
