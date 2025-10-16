def discr(a, b, c):
    D = b**2 - 4*a*c
    return D
a = float(input("Введи a: "))
b = float(input("Введи b: "))
c = float(input("Введи c: "))

if a == 0:
    print("не квадратне рівняння")
else:
    D = discr(a, b, c)
    print("D equals:", D)
    if D > 0:
        print("2 koreni")
    elif D == 0:
        print("1 korin'")
    else:
        print("Nemaye koreniv")
