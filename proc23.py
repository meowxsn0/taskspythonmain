#Функция even(k) возвращает True для чётного k. Найти количество чётных в наборе из 10 чисел
def even(k):
    return k % 2 == 0
cnt = 0
for i in range(10):
    k = int(input())
    if even(k):
        cnt += 1
print(cnt)