import math

a = float(input("Введите длину стороны: "))
n = int(input("Введите количество сторон: "))

if n < 3:
    print("Количество сторон должно быть не менее 3.")
else:
    perimeter = a * n

    area = (n * a ** 2) / (4 * math.tan(math.pi / n))

    print(f"Периметр: {perimeter}")
    print(f"Площадь: {area}")
