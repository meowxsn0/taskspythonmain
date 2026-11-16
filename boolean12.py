# Boolean14. Проверить истинность высказывания:
# «Ровно одно из чисел A, B, C положительное».
a = int(input())
b = int(input())
c = int(input())
cnt = (a > 0) + (b > 0) + (c > 0)
print(cnt == 1)
