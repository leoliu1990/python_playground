def swap_value(array, i, j):
  buffer = array[i]
  array[i] = array[j]
  array[j] = buffer


def partition(array, start, end):
  pivot = array[end]
  i = start
  j = end - 1

  while i < j:
    while array[j] > pivot and i < j:
      j -= 1
    while array[i] <= pivot and i < j:
      i += 1
    swap_value(array, i, j)
  swap_value(array, end, i + 1)
  return i + 1


def quick_sort(array, start, end):
  if start >= end:
    return

  mid = partition(array, start, end)
  quick_sort(array, start, mid - 1)
  quick_sort(array, mid + 1, end)


array = [4, 9, 6, 1, 8, 10, 2, 7, 5, 0, 3]
quick_sort(array, 0, len(array) - 1)
print(array)
