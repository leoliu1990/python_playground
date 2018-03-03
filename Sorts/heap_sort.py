def right_child(index):
  return (index + 1) * 2


def left_child(index):
  return (index + 1) * 2 - 1


def parent(index):
  return (index + 1) / 2 - 1


def swap_value(array, i, j):
  buffer = array[i]
  array[i] = array[j]
  array[j] = buffer


def max_heapify(array, heap_size, index):
  if index > heap_size:
    return
  largest = index
  if left_child(index) <= heap_size and array[left_child(index)] > array[index]:
    largest = left_child(index)
  if right_child(index) <= heap_size and array[right_child(index)] > array[largest]:
    largest = right_child(index)
  if largest != index:
    swap_value(array, index, largest)
    max_heapify(array, heap_size, largest)


def build_heap(array):
  for i in range(parent(len(array) - 1), -1, -1):
    max_heapify(array, len(array) - 1, i)


def heap_sort(array):
  build_heap(array)
  for i in range(len(array) - 1, 0, -1):
    swap_value(array, i, 0)
    max_heapify(array, i - 1, 0)


array = [4, 9, 6, 1, 8, 10, 2, 7, 5, 0, 3]
heap_sort(array)
print(array)
