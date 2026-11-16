# For3. Даны A и B (A < B). Вывести в порядке убывания все целые числа
# между A и B (не включая A и B) и их количество.
a = int(input())
b = int(input())
cnt = 0
for i in range(b - 1, a, -1):
    print(i)
    cnt += 1
print(cnt)