import random
array = [random.randint(1, 100) for num in range(20)]
print(array)
x = int(input("Введите x: "))
for num in array:
    if num == x:
        print("Число подходит")
        break