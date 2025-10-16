def test_list_functions():
    my_list = [1, 2, 3, 4, 5]
    print(f"Початковий: {my_list}")

    my_list.append(6)
    print(f"Після append(6): {my_list}")

    my_list.extend([7, 8])
    print(f"Після extend([7, 8]): {my_list}")

    my_list.insert(0, 0)
    print(f"Після insert(0, 0): {my_list}")

    my_list.remove(4)
    print(f"Після remove(4): {my_list}")

    my_list.reverse()
    print(f"Після reverse(): {my_list}")
    
    my_list.sort()
    print(f"Після sort(): {my_list}")

    new_list = my_list.copy()
    print(f"Створена копія списку: {new_list}")
    
    my_list.clear()
    print(f"Після clear(): {my_list}")

test_list_functions()