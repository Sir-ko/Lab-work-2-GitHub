print("Введите три стороны треугольника:")
a, b, c = float(input()), float(input()), float(input())
if a + b < c or a + c < b or b + c < a:
    print("Такого треугольника не существует!")
else:
    p = (a + b + c)/2 # полупериметр
    area = (p*(p-a)*(p-b)*(p-c))**0.5 # формула Герона
    print(f"{area:.2f}")