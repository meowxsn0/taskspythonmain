#Дан список из N строк. Вывести самую длинную и самую короткую строку (первую из
#встретившихся) и их длины
n = int(input())
a = []
for i in range(n):
    a.append(input())
long_s = a[0]
short_s = a[0]
for s in a:
    if len(s) > len(long_s):
        long_s = s
    if len(s) < len(short_s):
        short_s = s
print(long_s)
print(short_s)
print(len(long_s))
print(len(short_s))