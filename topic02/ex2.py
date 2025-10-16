def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "На нуль не ділять"
    return x / y
def calc_if_else():
    print("==============================")
    print("==========КАЛЬКУЛЯТОР=========")
    print("==============================")
    try:
        x = float(input("Введіть число x: "))
        операція = input("Введіть операцію (+, -, *, /): ")
        y = float(input("Введіть число y: "))
    except ValueError:
        print("Точно числа ввели?")
        return
    
    результат = None

    if операція == '+':
        результат = add(x, y)
    elif операція == '-':
        результат = subtract(x, y)
    elif операція == '*':
        результат = multiply(x, y)
    elif операція == '/':
        результат = divide(x, y)
    else:
        print("Невідома операція. Спробуйте +, -, *, або /.")
        return

    print(f"Результат: {x} {операція} {y} = {результат}")

calc_if_else()
