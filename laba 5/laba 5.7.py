import math
print("Введите координаты точки и радиус круга")
X = float(input("x = "))
Y = float(input("y = "))
R = float(input("R = "))

hypotenuse = math.sqrt(X ** 2 + Y ** 2)

if hypotenuse <= R:
    print("Точка принадлежит кругу")
else:
    print("Точка НЕ принадлежит кругу")