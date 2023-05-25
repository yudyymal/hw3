print('Сейчас вычислим, сколько раз встречается число X в массиве A[1..N]')

n = int(input("Введите натуральное число N - количество элементов в массиве: "))

a = []
for i in range(1, n + 1):
    a.append(i)
print(*a)

x = int(input("Введите число X: "))
print(x)

j = 0
for i in range(len(a)):
    if a[i] == x:
        j += 1

print(f'-> {j}')