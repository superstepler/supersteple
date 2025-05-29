try:
    number = int("привет")
    print(number)
except ValueError:
    print("Error. cannot output a string as an integer")
