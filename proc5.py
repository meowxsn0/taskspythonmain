#Proc6. Описать функцию digit_count_sum(k), возвращающую количество цифр и сумму цифр целого
#положительного числа k. Найти обе величины для пяти данных чисел.
def digit_count_sum(k):
    cnt = 0
    s = 0
    while k > 0:
        s += k % 10
        cnt += 1
        k //= 10
    return cnt, s
for i in range(5):
    k = int(input())
c, s = digit_count_sum(k)
print(c)
print(s)