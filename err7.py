# Err8. Читать числа до пустой строки; нечисловые строки
# пропускать со счётом. Вывести сумму и число пропусков.
s = 0
skipped = 0
while True:
    line = input()
    if line == "":
        break
    try:
        s += int(line)
    except ValueError:
        skipped += 1
        print("Пропущено: не число")
print(s)
print(skipped)