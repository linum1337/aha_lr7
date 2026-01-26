# analysis.py

import sys
sys.setrecursionlimit(10000)

import time
import random
from heap import MinHeap, MaxHeap
from heapsort import heapsort, heapsort_inplace
from priority_queue import PriorityQueue

def test_heap_operations():
    """Тестирование основных операций кучи"""
    print("="*70)
    print("ТЕСТИРОВАНИЕ ОПЕРАЦИЙ КУЧИ")
    print("="*70)

    # Тест Min-Heap
    print("\n1. Тест Min-Heap:")
    min_heap = MinHeap()
    values = [50, 30, 70, 20, 40, 60, 80, 10]

    print(f"   Вставка элементов: {values}")
    for val in values:
        min_heap.insert(val)

    print(f"   Содержимое массива кучи: {min_heap.heap}")
    print(f"   Минимум (peek): {min_heap.peek()}")
    print(f"   Куча валидна: {min_heap.is_valid_heap()}")

    print("\n   Визуализация min-heap:")
    print(min_heap.visualize())

    print("\n   Извлечение элементов:")
    extracted = []
    while not min_heap.is_empty():
        extracted.append(min_heap.extract())
    print(f"   Порядок извлечения: {extracted}")
    print(f"   ✓ Элементы извлечены в порядке возрастания: {extracted == sorted(values)}")

    # Тест Max-Heap
    print("\n2. Тест Max-Heap:")
    max_heap = MaxHeap()

    print(f"   Вставка элементов: {values}")
    for val in values:
        max_heap.insert(val)

    print(f"   Максимум (peek): {max_heap.peek()}")
    print(f"   Куча валидна: {max_heap.is_valid_heap()}")

    extracted = []
    while not max_heap.is_empty():
        extracted.append(max_heap.extract())
    print(f"   Порядок извлечения: {extracted}")
    print(f"   ✓ Элементы извлечены в порядке убывания: {extracted == sorted(values, reverse=True)}")

    # Тест build_heap
    print("\n3. Тест build_heap:")
    array = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35]
    print(f"   Исходный массив: {array}")

    heap = MinHeap()
    heap.build_heap(array)
    print(f"   После build_heap: {heap.heap}")
    print(f"   Куча валидна: {heap.is_valid_heap()}")

    print("\n" + "="*70)


def test_heapsort():
    """Тестирование сортировки кучей"""
    print("="*70)
    print("ТЕСТИРОВАНИЕ HEAPSORT")
    print("="*70)

    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3]
    ]

    print("\n1. Тест корректности (с дополнительной памятью):")
    for arr in test_arrays:
        sorted_arr = heapsort(arr)
        expected = sorted(arr)
        status = "✓" if sorted_arr == expected else "✗"
        print(f"   {status} {arr} → {sorted_arr}")

    print("\n2. Тест in-place heapsort:")
    for arr in test_arrays:
        arr_copy = arr.copy()
        heapsort_inplace(arr_copy)
        expected = sorted(arr)
        status = "✓" if arr_copy == expected else "✗"
        print(f"   {status} {arr} → {arr_copy}")

    print("\n" + "="*70)


def test_priority_queue():
    """Тестирование приоритетной очереди"""
    print("="*70)
    print("ТЕСТИРОВАНИЕ ПРИОРИТЕТНОЙ ОЧЕРЕДИ")
    print("="*70)

    pq = PriorityQueue()

    print("\n1. Добавление задач с приоритетами:")
    tasks = [
        ("Задача A", 5),
        ("Задача B", 1),
        ("Задача C", 3),
        ("Задача D", 2),
        ("Задача E", 4)
    ]

    for task, priority in tasks:
        pq.enqueue(task, priority)
        print(f"   Добавлена: {task} (приоритет {priority})")

    print(f"\n2. Размер очереди: {pq.size()}")
    print(f"   Следующая задача (peek): {pq.peek()}")

    print("\n3. Извлечение задач (в порядке приоритета):")
    order = []
    while not pq.is_empty():
        task = pq.dequeue()
        order.append(task)
        print(f"   Извлечена: {task}")

    expected_order = ["Задача B", "Задача D", "Задача C", "Задача E", "Задача A"]
    print(f"\n   ✓ Порядок корректный: {order == expected_order}")

    print("\n" + "="*70)


def compare_build_methods():
    """Сравнение методов построения кучи"""
    print("="*70)
    print("СРАВНЕНИЕ МЕТОДОВ ПОСТРОЕНИЯ КУЧИ")
    print("="*70)

    sizes = [1000, 5000, 10000, 20000, 50000]

    print(f"\n{'Размер':<10} {'Послед. вставка (с)':<22} {'build_heap (с)':<20} {'Ускорение'}")
    print("-" * 70)

    results = []

    for size in sizes:
        array = [random.randint(1, 100000) for _ in range(size)]

        # Метод 1: Последовательная вставка
        heap1 = MinHeap()
        start = time.time()
        for val in array:
            heap1.insert(val)
        time_insert = time.time() - start

        # Метод 2: build_heap
        heap2 = MinHeap()
        start = time.time()
        heap2.build_heap(array)
        time_build = time.time() - start

        speedup = time_insert / time_build if time_build > 0 else 0
        results.append({
            'size': size,
            'insert': time_insert,
            'build': time_build,
            'speedup': speedup
        })

        print(f"{size:<10} {time_insert:<22.6f} {time_build:<20.6f} {speedup:.2f}x")

    print("\n" + "="*70)
    return results


def compare_sorting_algorithms():
    """Сравнение Heapsort с другими алгоритмами сортировки"""
    print("="*70)
    print("СРАВНЕНИЕ АЛГОРИТМОВ СОРТИРОВКИ")
    print("="*70)

    sizes = [1000, 5000, 10000, 20000]

    print(f"\n{'Размер':<10} {'Heapsort (с)':<15} {'QuickSort (с)':<18} {'MergeSort (с)':<18} {'sorted() (с)'}")
    print("-" * 80)

    results = []

    for size in sizes:
        array = [random.randint(1, 100000) for _ in range(size)]

        # Heapsort
        arr_heap = array.copy()
        start = time.time()
        heapsort_inplace(arr_heap)
        time_heap = time.time() - start

        # QuickSort (встроенная сортировка Python использует Timsort)
        arr_quick = array.copy()
        start = time.time()
        quicksort(arr_quick, 0, len(arr_quick) - 1)
        time_quick = time.time() - start

        # MergeSort
        arr_merge = array.copy()
        start = time.time()
        mergesort(arr_merge)
        time_merge = time.time() - start

        # Встроенная сортировка Python (Timsort)
        arr_sorted = array.copy()
        start = time.time()
        arr_sorted.sort()
        time_sorted = time.time() - start

        results.append({
            'size': size,
            'heapsort': time_heap,
            'quicksort': time_quick,
            'mergesort': time_merge,
            'timsort': time_sorted
        })

        print(f"{size:<10} {time_heap:<15.6f} {time_quick:<18.6f} {time_merge:<18.6f} {time_sorted:.6f}")

    print("\n" + "="*70)
    return results


def quicksort(arr, low, high):
    """Быстрая сортировка для сравнения"""
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def partition(arr, low, high):
    """Разделение для быстрой сортировки"""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def mergesort(arr):
    """Сортировка слиянием для сравнения"""
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    test_heap_operations()
    print("\n")

    test_heapsort()
    print("\n")

    test_priority_queue()
    print("\n")

    build_results = compare_build_methods()
    print("\n")

    sort_results = compare_sorting_algorithms()
