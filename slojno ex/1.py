array = [33, 10 ,5 ,1]
print(array)
n = len(array)
for i in range(n - 1):
    for j in range(n - 1 -i):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
print(array)