import random
array_1 = [random.randint(1,100) for num in range(15)]
print(array_1)
array = []
for num in array_1:
    if num % 2 == 0:
        array.append(num)
sort_array = sorted(array)
print(sort_array)

