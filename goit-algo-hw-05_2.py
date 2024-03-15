def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Якщо значення не знайдено, повертаємо None
    return (iterations, arr[right])

# Приклад використання:
arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
target = 0.55
iterations, upper_bound = binary_search(arr, target)
print("Кількість ітерацій:", iterations)
print("Верхня межа:", upper_bound)
