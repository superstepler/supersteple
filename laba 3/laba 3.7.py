number = int(input("Введите число: "))
def definition(number):
    str_number = str(number)
    for num in range(len(str_number)):
        if int(str_number[num]) > int(str_number[num + 1]):
            print("Числа по убыванию")
            return
print(definition(number))