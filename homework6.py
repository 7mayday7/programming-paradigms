def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Элемент не найден


if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target_element = 6

    result = binary_search(sorted_array, target_element)

    if result != -1:
        print(f"Элемент {target_element} найден по индексу {result}.")
    else:
        print(f"Элемент {target_element} не найден в массиве.")
