# Алгоритм 1: Сортировка пузырьком (Bubble Sort)
def bubble_sort(mas):
    n = len(mas)
    for run in range(n - 1):
        for i in range(n - 1 - run):
            if mas[i] > mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
    return mas


# Алгоритм 2: Быстрая сортировка (Quick Sort)
def quick_sort(s):
    if len(s) <= 1:
        return s
    element = s[0]
    left = [i for i in s if i < element]
    center = [i for i in s if i == element]
    right = [i for i in s if i > element]
    return quick_sort(left) + center + quick_sort(right)


# Алгоритм 3: Сортировка выбором (Selection Sort)
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Демонстрация работы алгоритмов
if __name__ == "__main__":
    print("=" * 50)
    print("Сортировка пузырьком (Bubble Sort)")
    arr1 = [5, 7, 4, 3, 8, 2]
    print(f"Исходный массив: {arr1}")
    print(f"Отсортированный: {bubble_sort(arr1[:])}")  # Используем копию массива

    print("\n" + "=" * 50)
    print("Быстрая сортировка (Quick Sort)")
    arr2 = [5, 2, 9, 0, 1, 5, 3]
    print(f"Исходный массив: {arr2}")
    print(f"Отсортированный: {quick_sort(arr2)}")  # Возвращает новый список

    print("\n" + "=" * 50)
    print("Сортировка выбором (Selection Sort)")
    arr3 = [64, 25, 12, 22, 11]
    print(f"Исходный массив: {arr3}")
    print(f"Отсортированный: {selection_sort(arr3[:])}")  # Используем копию массива

    print("\n" + "=" * 50)
    print("Сравнение работы всех алгоритмов на одном наборе данных")
    test_data = [9, 3, 7, 1, 8, 2, 5]
    print(f"Тестовые данные: {test_data}")
    print(f"Пузырьковая: {bubble_sort(test_data[:])}")
    print(f"Быстрая:     {quick_sort(test_data)}")
    print(f"Выбором:     {selection_sort(test_data[:])}")