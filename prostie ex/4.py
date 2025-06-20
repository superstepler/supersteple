string = input("Введите строку: ")
rever = string[::-1]
if string == rever:
    print(string)
else:
    print("не палиндром")