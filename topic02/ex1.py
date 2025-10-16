import math
def discr(a, b, c):
    """Обчислює дискримінант D."""
    D = b**2 - 4*a*c
    return D
try:
    a = float(input("Введи a: "))
    b = float(input("Введи b: "))
    c = float(input("Введи c: "))
except ValueError:
    print("Введено некоректне число")
    exit()

if a == 0:
    print("Це не квадратне рівняння")
else:
    D = discr(a, b, c)
    print(f"\nДискримінант дорівнює: {D}")
 
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("Маємо 2 різні дійсні корені:")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")
    elif D == 0:
        x = -b / (2 * a)
        print("Маємо 1 дійсний корінь ")
        print(f"x = {x:.2f}")
    else:
        print("Дискримінант від'ємний ")