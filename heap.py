# heap.py

class Heap:
    """
    Универсальная реализация кучи (heap) на основе массива
    Поддерживает min-heap и max-heap
    """

    def __init__(self, is_min=True):
        """
        Инициализация кучи

        Args:
            is_min: True для min-heap, False для max-heap
        """
        self.heap = []
        self.is_min = is_min

    def _compare(self, a, b):
        """Сравнение элементов в зависимости от типа кучи"""
        if self.is_min:
            return a < b
        else:
            return a > b

    def _parent(self, index):
        """Индекс родителя узла"""
        return (index - 1) // 2

    def _left_child(self, index):
        """Индекс левого потомка"""
        return 2 * index + 1

    def _right_child(self, index):
        """Индекс правого потомка"""
        return 2 * index + 2

    def _sift_up(self, index):
        """
        Всплытие элемента вверх для восстановления свойства кучи
        Временная сложность: O(log n)
        """
        parent = self._parent(index)

        # Пока не достигли корня и элемент нарушает свойство кучи
        while index > 0 and self._compare(self.heap[index], self.heap[parent]):
            # Меняем местами с родителем
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent(index)

    def _sift_down(self, index):
        """
        Погружение элемента вниз для восстановления свойства кучи
        Временная сложность: O(log n)
        """
        size = len(self.heap)

        while True:
            extreme = index  # Индекс элемента с экстремальным значением (мин или макс)
            left = self._left_child(index)
            right = self._right_child(index)

            # Сравниваем с левым потомком
            if left < size and self._compare(self.heap[left], self.heap[extreme]):
                extreme = left

            # Сравниваем с правым потомком
            if right < size and self._compare(self.heap[right], self.heap[extreme]):
                extreme = right

            # Если свойство кучи не нарушено, выходим
            if extreme == index:
                break

            # Меняем местами и продолжаем погружение
            self.heap[index], self.heap[extreme] = self.heap[extreme], self.heap[index]
            index = extreme

    def insert(self, value):
        """
        Вставка элемента в кучу
        Временная сложность: O(log n)
        """
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract(self):
        """
        Извлечение корня (минимума или максимума)
        Временная сложность: O(log n)

        Returns:
            Корневой элемент

        Raises:
            IndexError: Если куча пустая
        """
        if len(self.heap) == 0:
            raise IndexError("Куча пустая")

        if len(self.heap) == 1:
            return self.heap.pop()

        # Сохраняем корень
        root = self.heap[0]

        # Перемещаем последний элемент в корень
        self.heap[0] = self.heap.pop()

        # Восстанавливаем свойство кучи
        self._sift_down(0)

        return root

    def peek(self):
        """
        Просмотр корня без извлечения
        Временная сложность: O(1)

        Returns:
            Корневой элемент

        Raises:
            IndexError: Если куча пустая
        """
        if len(self.heap) == 0:
            raise IndexError("Куча пустая")
        return self.heap[0]

    def build_heap(self, array):
        """
        Построение кучи из произвольного массива (алгоритм heapify)
        Временная сложность: O(n) - более эффективно, чем n вставок O(n log n)

        Args:
            array: Массив элементов
        """
        self.heap = array.copy()

        # Начинаем с последнего узла, имеющего потомков
        # и двигаемся к корню
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._sift_down(i)

    def size(self):
        """Размер кучи"""
        return len(self.heap)

    def is_empty(self):
        """Проверка на пустоту"""
        return len(self.heap) == 0

    def is_valid_heap(self):
        """
        Проверка корректности свойства кучи
        Временная сложность: O(n)
        """
        for i in range(len(self.heap)):
            left = self._left_child(i)
            right = self._right_child(i)

            # Проверяем левого потомка
            if left < len(self.heap):
                if self.is_min and self.heap[i] > self.heap[left]:
                    return False
                if not self.is_min and self.heap[i] < self.heap[left]:
                    return False

            # Проверяем правого потомка
            if right < len(self.heap):
                if self.is_min and self.heap[i] > self.heap[right]:
                    return False
                if not self.is_min and self.heap[i] < self.heap[right]:
                    return False

        return True

    def visualize(self):
        """
        Текстовая визуализация кучи в виде дерева
        """
        if not self.heap:
            return "Куча пустая"

        result = []
        self._visualize_helper(0, "", True, result)
        return '\n'.join(result)

    def _visualize_helper(self, index, prefix, is_tail, result):
        """Рекурсивная визуализация"""
        if index >= len(self.heap):
            return

        right = self._right_child(index)
        if right < len(self.heap):
            new_prefix = prefix + ("│   " if is_tail else "    ")
            self._visualize_helper(right, new_prefix, False, result)

        result.append(prefix + ("└── " if is_tail else "┌── ") + str(self.heap[index]))

        left = self._left_child(index)
        if left < len(self.heap):
            new_prefix = prefix + ("    " if is_tail else "│   ")
            self._visualize_helper(left, new_prefix, True, result)


class MinHeap(Heap):
    """Min-heap: корень - минимальный элемент"""
    def __init__(self):
        super().__init__(is_min=True)


class MaxHeap(Heap):
    """Max-heap: корень - максимальный элемент"""
    def __init__(self):
        super().__init__(is_min=False)
