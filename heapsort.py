# heapsort.py

from heap import MaxHeap

def heapsort(array):
    """
    Сортировка кучей (использует дополнительную память для кучи)

    Алгоритм:
    1. Строим max-heap из массива
    2. Последовательно извлекаем максимум и добавляем в результат

    Временная сложность: O(n log n)
    Пространственная сложность: O(n)

    Args:
        array: Массив для сортировки

    Returns:
        Отсортированный массив
    """
    if len(array) <= 1:
        return array.copy()

    # Создаем max-heap и строим из массива
    heap = MaxHeap()
    heap.build_heap(array)

    # Извлекаем элементы в обратном порядке
    result = []
    while not heap.is_empty():
        result.append(heap.extract())

    # Переворачиваем (т.к. извлекали максимумы)
    result.reverse()

    return result


def heapsort_inplace(array):
    """
    In-place сортировка кучей (без дополнительной памяти)

    Алгоритм:
    1. Строим max-heap из массива (модифицируя его на месте)
    2. Последовательно извлекаем максимум (корень) и помещаем его в конец
    3. Уменьшаем размер кучи и восстанавливаем свойство

    Временная сложность: O(n log n)
    Пространственная сложность: O(1)

    Args:
        array: Массив для сортировки (модифицируется)
    """
    n = len(array)

    if n <= 1:
        return

    # Шаг 1: Построение max-heap
    # Начинаем с последнего родительского узла
    for i in range(n // 2 - 1, -1, -1):
        _sift_down_inplace(array, i, n)

    # Шаг 2: Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        # Перемещаем корень (максимум) в конец
        array[0], array[i] = array[i], array[0]

        # Восстанавливаем свойство кучи для уменьшенной кучи
        _sift_down_inplace(array, 0, i)


def _sift_down_inplace(array, index, heap_size):
    """
    Погружение элемента для in-place heapsort

    Args:
        array: Массив (содержит кучу)
        index: Индекс элемента для погружения
        heap_size: Текущий размер кучи
    """
    while True:
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # Находим наибольший из трех элементов
        if left < heap_size and array[left] > array[largest]:
            largest = left

        if right < heap_size and array[right] > array[largest]:
            largest = right

        # Если свойство max-heap не нарушено, выходим
        if largest == index:
            break

        # Меняем местами и продолжаем
        array[index], array[largest] = array[largest], array[index]
        index = largest


def compare_heapsort_methods(array):
    """
    Сравнение двух методов heapsort

    Returns:
        dict с результатами
    """
    import time

    # Метод 1: С дополнительной памятью
    arr1 = array.copy()
    start = time.time()
    result1 = heapsort(arr1)
    time1 = time.time() - start

    # Метод 2: In-place
    arr2 = array.copy()
    start = time.time()
    heapsort_inplace(arr2)
    time2 = time.time() - start

    return {
        'with_extra_memory': time1,
        'inplace': time2,
        'speedup': time1 / time2 if time2 > 0 else 0
    }
