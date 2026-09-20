def correct_input(f: int = 0, t: int = 0, any: bool = False) -> float:
    while True: # ожидание корректного ввода пользователем
        print("Enter a value: ", end='')
        try:
            val = float(input().strip().replace(',', '.'))
        except ValueError:
            print("Incorrect value, try again")
            continue
        if (not any and val.is_integer() and f <= val <= t) or any:
            return val


print("From:", "1) kilometers", "2) meters", "3) centimeters", "4) millimeters", "5) miles", "6) yards", sep='\n')
fr = int(correct_input(1, 6)) # из какой величины переводим
print("To:", "1) kilometers", "2) meters", "3) centimeters", "4) millimeters", "5) miles", "6) yards", sep='\n')
to = int(correct_input(1, 6)) # в какую величину переводим
print("Please, provide value for conversion: ", end='\n')
val = correct_input(any=True)
meters_ratio = {1: 1000, 2: 1, 3: 0.01, 4: 0.001, 5: 1_609.34, 6: 0.9144}
in_meters = val * meters_ratio[fr] # перевод сначала в метры
in_needed = in_meters / meters_ratio[to] # перевод в нужную величину
names_dict = {1: "km", 2: "m", 3: "cm", 4: "mm", 5: "mi", 6: "yd"}
print(f"Answer: {val:.2f} {names_dict[fr]} -> {in_needed:.2f} {names_dict[to]}")