array = [1,2,3,8,7,6,4,5]
print(array)
array_sort = sorted(array)
print(array_sort)
max_num = max(array_sort)
max_index = array_sort.index(max_num)
two = max_index - 1
max_two = array_sort[two]
print(max_two)
