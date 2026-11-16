#begin28. Дано число A. Вычислить A15, используя две вспомогательные переменные и пять операций умножения. 
#Для этого последовательно находить A2, A3, A5, A10, A15. Вывести все найденные степени числа A.
a = float(input())
t = a * a
print(t)
temp1 = t * a 
print(temp1)
temp1 = temp1 * t
print(temp1)
t = temp1 * temp1
print(t)
temp1 = temp1 * t
print(temp1)
