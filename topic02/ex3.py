
def add(x, y):
    """Повертає суму двох чисел."""
    return x + y

def subtract(x, y):
    """Повертає різницю двох чисел."""
    return x - y

def multiply(x, y):
    """Повертає добуток двох чисел."""
    return x * y

def divide(x, y):
    """Повертає частку. Перевіряє ділення на нуль."""
    if y == 0:
        return "На нуль не ділять"
    return x / y

def calc_match_case():
    print("==============================")
    print("=====КАЛЬКУЛЯТОР (MATCH)======")
    print("==============================")

    try:
        x = float(input("Введіть число x: "))
        операція = input("Введіть операцію (+, -, *, /): ")
        y = float(input("Введіть число y: "))
    except ValueError:
        print("Точно числа ввели?")
        return
    
    результат = None

    match операція:
        case '+':
            результат = add(x, y)
        case '-':
            результат = subtract(x, y)
        case '*':
            результат = multiply(x, y)
        case '/':
            результат = divide(x, y)
        case _: 
            print("Невідома операція. Спробуйте +, -, *, або /.")
            return

    print(f"Результат: {x} {операція} {y} = {результат}")

calc_match_case()