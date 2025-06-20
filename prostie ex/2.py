array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = int(input("Введите N: "))
array_1 = array[0:num]
array_2 = []
for i in array_1:
    if i % 2 == 0:
        array_2.append(i)
print(array)
print(array_2)

