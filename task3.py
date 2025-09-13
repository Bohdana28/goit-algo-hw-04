import random
import timeit

# Алгоритми сортування

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def timsort(arr):
    return sorted(arr)


# Генерація тестових даних

def generate_data(size):
    return [random.randint(0, 1000000) for _ in range(size)]


# Порівняння алгоритмів

def compare_sorts():
    sizes = [100, 1000, 5000]  
    algorithms = [("Merge Sort", merge_sort),
                  ("Insertion Sort", insertion_sort),
                  ("Timsort", timsort)]

    for size in sizes:
        data = generate_data(size)
        print(f"\nМасив розміром: {size}")
        for name, func in algorithms:
            # Використовуємо lambda, щоб передавати нову копію масиву
            t = timeit.timeit(lambda: func(data), number=5)
            print(f"{name:15}: {t:.5f} секунд")

    print("\nВисновок:")
    print("Insertion Sort швидкий тільки на малих масивах.")
    print("Merge Sort працює стабільно і краще масштабується.")
    print("Timsort найшвидший, тому в Python його і використовують за замовчуванням.")


# Запуск

if __name__ == "__main__":
    compare_sorts()