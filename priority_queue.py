# priority_queue.py

from heap import MinHeap

class PriorityQueue:
    """
    Приоритетная очередь на основе min-heap
    Элементы с меньшим приоритетом извлекаются первыми
    """

    def __init__(self):
        """Инициализация приоритетной очереди"""
        self.heap = MinHeap()
        self.counter = 0  # Счетчик для сохранения порядка при равных приоритетах

    def enqueue(self, item, priority):
        """
        Добавление элемента с приоритетом
        Временная сложность: O(log n)

        Args:
            item: Элемент для добавления
            priority: Приоритет (меньше = выше приоритет)
        """
        # Используем кортеж (priority, counter, item)
        # counter нужен для стабильной сортировки при равных приоритетах
        self.heap.insert((priority, self.counter, item))
        self.counter += 1

    def dequeue(self):
        """
        Извлечение элемента с наивысшим приоритетом (наименьшим значением)
        Временная сложность: O(log n)

        Returns:
            Элемент с наивысшим приоритетом

        Raises:
            IndexError: Если очередь пустая
        """
        if self.is_empty():
            raise IndexError("Очередь пустая")

        priority, _, item = self.heap.extract()
        return item

    def peek(self):
        """
        Просмотр элемента с наивысшим приоритетом без извлечения
        Временная сложность: O(1)

        Returns:
            Элемент с наивысшим приоритетом

        Raises:
            IndexError: Если очередь пустая
        """
        if self.is_empty():
            raise IndexError("Очередь пустая")

        priority, _, item = self.heap.peek()
        return item

    def is_empty(self):
        """Проверка на пустоту"""
        return self.heap.is_empty()

    def size(self):
        """Размер очереди"""
        return self.heap.size()


class MaxPriorityQueue:
    """
    Приоритетная очередь на основе max-heap
    Элементы с большим приоритетом извлекаются первыми
    """

    def __init__(self):
        """Инициализация приоритетной очереди"""
        from heap import MaxHeap
        self.heap = MaxHeap()
        self.counter = 0

    def enqueue(self, item, priority):
        """
        Добавление элемента с приоритетом
        Временная сложность: O(log n)

        Args:
            item: Элемент для добавления
            priority: Приоритет (больше = выше приоритет)
        """
        # Используем кортеж (priority, -counter, item)
        # -counter для обратного порядка при равных приоритетах
        self.heap.insert((priority, -self.counter, item))
        self.counter += 1

    def dequeue(self):
        """
        Извлечение элемента с наивысшим приоритетом (наибольшим значением)
        Временная сложность: O(log n)

        Returns:
            Элемент с наивысшим приоритетом

        Raises:
            IndexError: Если очередь пустая
        """
        if self.is_empty():
            raise IndexError("Очередь пустая")

        priority, _, item = self.heap.extract()
        return item

    def peek(self):
        """
        Просмотр элемента с наивысшим приоритетом без извлечения
        Временная сложность: O(1)

        Returns:
            Элемент с наивысшим приоритетом

        Raises:
            IndexError: Если очередь пустая
        """
        if self.is_empty():
            raise IndexError("Очередь пустая")

        priority, _, item = self.heap.peek()
        return item

    def is_empty(self):
        """Проверка на пустоту"""
        return self.heap.is_empty()

    def size(self):
        """Размер очереди"""
        return self.heap.size()
