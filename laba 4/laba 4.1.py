import random
array = []
ran_array = [random.randint(1, 100) for num in range(15)]
for i in range(15):
    array.append(ran_array[i])
print(array)