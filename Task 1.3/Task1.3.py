def correct_input() -> int:
    while True: # ожидание корректного ввода пользователем
        print("Enter a value: ", end='')
        try:
            val = int(input().strip())
        except ValueError:
            print("Incorrect value, try again") 
            continue
        return val


print("Enter a year to decide whether it's a leap one or not:")
year = correct_input()
# проверка на високосный год
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: 
    print("It's a leap year!")
else:
    print("It's not a leap year...")