def add(x, y):
    """Ця функція додає два числа."""
    return x + y

def subtract(x, y):
    """Ця функція віднімає два числа."""
    return x - y

def multiply(x, y):
    """Ця функція множить два числа."""
    return x * y

def divide(x, y):
    """Ця функція ділить два числа.
    Може викликати виняток ZeroDivisionError."""

    return x / y

def calculator():
    """Основна функція калькулятора з безперервним циклом."""
    print("==============================")
    print("==========КАЛЬКУЛЯТОР=========")
    print("==============================")
    
    while True:
        x_str = input("Введіть перше число (або 'q' для виходу): ")
        
        if x_str.lower() == 'q':
            break
            
        операція = input("Введіть операцію (+, -, *, /): ")
        y_str = input("Введіть друге число: ")
        
        try:

            x = float(x_str)
            y = float(y_str)
            
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
                print("-" * 30)
                continue
            
            print(f"Результат: {x} {операція} {y} = {результат}")

        except ValueError:
            print("Помилка: Введено не число. Спробуйте ще раз.")
        except ZeroDivisionError:
            print("Помилка: На нуль ділити не можна")
        
        finally:
            print("-" * 30)
    print("Калькулятор завершує роботу. До побачення!")
calculator()