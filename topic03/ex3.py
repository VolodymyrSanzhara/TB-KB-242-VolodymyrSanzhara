def test_dict_functions():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(f"Початковий словник: {my_dict}")

    print("\n--- Тестування update ---")
    my_dict.update({'d': 4, 'b': 22})
    print(f"Після update({{'d': 4, 'b': 22}}): {my_dict}")

    print("\n--- Тестування del ---")
    del my_dict['a']
    print(f"Після del ['a']: {my_dict}")

    print("\n--- Тестування keys ---")
    keys = my_dict.keys()
    print(f"Ключі словника: {list(keys)}")

    print("\n--- Тестування values ---")
    values = my_dict.values()
    print(f"Значення словника: {list(values)}")

    print("\n--- Тестування items ---")
    items = my_dict.items()
    print(f"Пари 'ключ-значення': {list(items)}")
    
    print("\n--- Тестування clear ---")
    my_dict.clear()
    print(f"Після clear: {my_dict}")

test_dict_functions()