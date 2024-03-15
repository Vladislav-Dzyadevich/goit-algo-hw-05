import timeit

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Функція для вимірювання часу виконання алгоритму пошуку підрядка
def measure_search_algorithm(text, pattern, algorithm):
    stmt = f"{algorithm}('{text}', '{pattern}')"
    setup = f"from __main__ import {algorithm}"
    execution_time = timeit.timeit(stmt, setup=setup, number=10)
    return execution_time / 10  # Середній час виконання за 10 повторень

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1

    return -1

# Алгоритм Кнута-Морріса-Пратта
def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    prefix = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                return i - m + 1
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    p = 31
    modulus = 10**9 + 9
    pattern_hash = 0
    text_hash = 0
    p_pow = 1
    for i in range(m):
        pattern_hash = (pattern_hash + (ord(pattern[i]) - ord('a') + 1) * p_pow) % modulus
        text_hash = (text_hash + (ord(text[i]) - ord('a') + 1) * p_pow) % modulus
        p_pow = (p_pow * p) % modulus
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            text_hash = (text_hash - (ord(text[i]) - ord('a') + 1) * p_pow) % modulus
            text_hash = (text_hash * p + (ord(text[i + m]) - ord('a') + 1)) % modulus
            text_hash = (text_hash + modulus) % modulus
    return -1

# Читаємо тексти з файлів
text1 = read_file("art1.txt")
text2 = read_file("art2.txt")

# Задаємо підрядки для пошуку
pattern1_existing = "Кожна система містить набір обмежень і вимог"
pattern1_nonexistent = "івфвафіа"
pattern2_existing = "Вікіпедія GPGPU"
pattern2_nonexistent = "фцвфцвфВФ"

# Вимірюємо час виконання кожного алгоритму для кожного тексту та підрядка
algorithms = ["boyer_moore", "kmp", "rabin_karp"]
for algorithm in algorithms:
    time1_existing = measure_search_algorithm(text1, pattern1_existing, algorithm)
    time1_nonexistent = measure_search_algorithm(text1, pattern1_nonexistent, algorithm)
    time2_existing = measure_search_algorithm(text2, pattern2_existing, algorithm)
    time2_nonexistent = measure_search_algorithm(text2, pattern2_nonexistent, algorithm)

    print(f"Алгоритм: {algorithm}")
    print("Стаття 1:")
    print("Існуючий підрядок:", time1_existing)
    print("неіснуючий підрядок:", time1_nonexistent)
    print("Стаття 2:")
    print("Існуючий підрядок:", time2_existing)
    print("неіснуючий підрядок:", time2_nonexistent)
    print()
