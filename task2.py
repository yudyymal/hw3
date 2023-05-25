print('Сейчас найдём в массиве A[1..N] самый близкий по величине элемент к заданному числу X')

n = int(input("Введите натуральное число N - количество элементов в массиве: "))

a = []
for i in range(1, n + 1):
    a.append(i)
print(*a)

x = float(input("Введите число X: "))
print(x)

dif = abs(x - a[0])
near = a[0]
for i in range(len(a)):
    if abs(x - a[i]) < dif:
        dif = abs(x - a[i])
        near = a[i]

print(f'-> {near}')