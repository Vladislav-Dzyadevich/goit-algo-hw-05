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

    # Після завершення циклу визначаємо верхню межу
    if right < 0:
        return (iterations, None)  # Якщо right < 0, значить масив порожній
    elif left >= len(arr):
        return (iterations, arr[right])  # Якщо left >= len(arr), значить target більший за всі елементи
    else:
        # В іншому випадку, верхня межа - елемент, що стоїть правіше від mid,
        # або максимальне значення з масиву, якщо target більше за всі елементи
        return (iterations, arr[left] if target > arr[right] else arr[right])

# Приклад використання:
arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
target = 0.55
iterations, upper_bound = binary_search(arr, target)
print("Кількість ітерацій:", iterations)
print("Верхня межа:", upper_bound)
