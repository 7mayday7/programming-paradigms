# Императивный стиль
def sort_list_imperative(list_number):
    n = len(list_number)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if list_number[j] < list_number[j + 1]:
                list_number[j], list_number[j + 1] = list_number[j + 1], list_number[j]
                swapped = True

        if not swapped:
            break


# Декларативный стиль
def sort_list_declarative(list_number):
    sorted_list = sorted(list_number, reverse=True)
    return sorted_list


# Пример использования:
numbers = [4, 2, 8, 1, 7]

sort_list_imperative(numbers)
print("Отсортированный список в порядке убывания:", numbers)

sorted_numbers = sort_list_declarative(numbers)
print("Отсортированный список в порядке убывания:", sorted_numbers)
