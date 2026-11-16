# Err4. Прочитать целое число; в else вывести 100 / n,
# в finally вывести "Вычисление завершено".
try:
    n = int(input())
    res = 100 / n
except ValueError:
    print("Ошибка ввода")
except ZeroDivisionError:
    print("Делить на ноль нельзя")
else:
    print(res)
finally:
    print("Вычисление завершено")   