length = int(input("Введите длину прямоугольника: "))
height = int(input("Введите высоту прямоугольника: "))
square = int(input("Введите стороны квадрата(одно число): "))
def figures():
    area_rectangle = height * length
    area_square = square * square
    squares = area_rectangle / area_square
    return squares
print(f"Число квадратов: {figures()}")