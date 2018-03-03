def merge_sort(array):
  if len(array) < 2:
    return array
  ind_mid = len(array) / 2
  left_array = merge_sort(array[:ind_mid])
  right_array = merge_sort(array[ind_mid:])

  i = 0
  j = 0
  k = 0
  while i < len(left_array) and j < len(right_array):
    if left_array[i] < right_array[j]:
      array[k] = left_array[i]
      i += 1
    else:
      array[k] = right_array[j]
      j += 1
    k += 1
  while i < len(left_array):
    array[k] = left_array[i]
    i += 1
    k += 1
  while j < len(right_array):
    array[k] = right_array[j]
    j += 1
    k += 1

  return array


array = [9,6,4,8,2,5,0,1]
sorted_array = merge_sort(array)
print(sorted_array)