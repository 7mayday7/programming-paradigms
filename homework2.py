n = int(input("Введите число n: "))
print(f"Таблица умножения от 1 до {n}:")
for i in range(1, n + 1):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
