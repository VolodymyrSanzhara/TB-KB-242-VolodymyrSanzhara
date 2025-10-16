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

def calculator():
    print("==============================")
    print("==========КАЛЬКУЛЯТОР=========")
    print("==============================")
    
    while True:
        try:
            x_str = input("Введіть перше число (або 'q' для виходу): ")
            if x_str.lower() == 'q':
                break
            x = float(x_str)
            
            операція = input("Введіть операцію (+, -, *, /): ")
            
            y_str = input("Введіть друге число: ")
            y = float(y_str)
            
        except ValueError:
            print("Точно числа ввели? Спробуйте ще раз.")
            continue
        
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
            continue

        print(f"Результат: {x} {операція} {y} = {результат}")
        
    print("Калькулятор завершує роботу.")

calculator()