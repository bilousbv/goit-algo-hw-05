# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Алгоритм Боєра-Мура
def boyer_moore_search(text, pattern):
    def build_last(pattern):
        last = {}
        for i in range(len(pattern)):
            last[pattern[i]] = i
        return last

    last = build_last(pattern)
    m = len(pattern)
    n = len(text)
    i = m - 1
    j = m - 1
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            lo = last.get(text[i], -1)  # Використовуємо .get() для безпечного отримання значення
            i += m - min(j, 1 + lo)
            j = m - 1
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp_search(text, pattern):
    d = 256  # Кількість символів в ASCII
    q = 101  # Просте число для обчислення хешів
    m = len(pattern)
    n = len(text)
    p = 0    # хеш для шаблону
    t = 0    # хеш для тексту
    h = 1

    # Значення h = d^(m-1) % q
    for i in range(m - 1):
        h = (h * d) % q

    # Обчислення хешу для шаблону та першого вікна тексту
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Пошук шаблону
    for i in range(n - m + 1):
        # Перевірка на відповідність хешу
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

import timeit

# Функція для вимірювання часу роботи алгоритму
def measure_time(search_func, text, pattern):
    return timeit.timeit(lambda: search_func(text, pattern), number=1)

# Читання тексту з файлів
with open("Task3/article1.txt", "r") as f:
    text1 = f.read()
with open("Task3/article2.txt", "r") as f:
    text2 = f.read()

# Підрядки для пошуку (приклади)
text1_existing_substring = "Розглянемо простий приклад завдання"  # Підрядок, що існує в статті 1
text2_existing_substring = "Зменшення розміру блоку дозволяє зменшити втрати пам’яті"  # Підрядок, що існує в статті 2
non_existing_substring = "nonexistentpattern"  # Підрядок, що не існує

# Тестування на першому тексті
print("Тестування на article1.txt")
print("Алгоритм Кнута-Морріса-Пратта:")
print("Існуючий підрядок:", measure_time(kmp_search, text1, text1_existing_substring))
print("Неіснуючий підрядок:", measure_time(kmp_search, text1, non_existing_substring))

print("\nАлгоритм Боєра-Мура:")
print("Існуючий підрядок:", measure_time(boyer_moore_search, text1, text1_existing_substring))
print("Неіснуючий підрядок:", measure_time(boyer_moore_search, text1, non_existing_substring))

print("\nАлгоритм Рабіна-Карпа:")
print("Існуючий підрядок:", measure_time(rabin_karp_search, text1, text1_existing_substring))
print("Неіснуючий підрядок:", measure_time(rabin_karp_search, text1, non_existing_substring))

# Тестування на другому тексті
print("\nТестування на article2.txt")
print("Алгоритм Кнута-Морріса-Пратта:")
print("Існуючий підрядок:", measure_time(kmp_search, text2, text2_existing_substring))
print("Неіснуючий підрядок:", measure_time(kmp_search, text2, non_existing_substring))

print("\nАлгоритм Боєра-Мура:")
print("Існуючий підрядок:", measure_time(boyer_moore_search, text2, text2_existing_substring))
print("Неіснуючий підрядок:", measure_time(boyer_moore_search, text2, non_existing_substring))

print("\nАлгоритм Рабіна-Карпа:")
print("Існуючий підрядок:", measure_time(rabin_karp_search, text2, text2_existing_substring))
print("Неіснуючий підрядок:", measure_time(rabin_karp_search, text2, non_existing_substring))