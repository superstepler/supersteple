import random
random_number = random.randint(1, 25)
array = []
for num in range(random_number):
    number = 3 * random_number
    number -= 3
    array.append(number)
print(f"Массив: {array}")