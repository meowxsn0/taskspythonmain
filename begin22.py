#begin23. Даны переменные A, B, C. 
#Изменить их значения, переместив содержимое A в B, B — в C, C — в A, и вывести новые значения переменных A, B, C.
a = float(input())
b = float(input())
c = float(input())
t = a
a = b
b = c
c = t 
print(a)
print(b)
print(c)
