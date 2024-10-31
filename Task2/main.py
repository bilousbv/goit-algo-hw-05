def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return iterations, arr[mid]

        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Якщо елемент не знайдено, то upper_bound залишається найближчим елементом більшим за target
    return iterations, upper_bound

# Приклад використання
arr = [0.1, 0.5, 1.3, 2.4, 3.6, 4.8, 5.9]
target = 2.5
result = binary_search(arr, target)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")