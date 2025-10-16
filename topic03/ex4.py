import bisect

def find_insertion_position(sorted_list, new_element):
    position = bisect.bisect_left(sorted_list, new_element)
    return position


my_sorted_list = [10, 20, 30, 40, 50, 60]
element_to_add = 35

pos = find_insertion_position(my_sorted_list, element_to_add)
print(f"Відсортований список: {my_sorted_list}")
print(f"Елемент для вставки: {element_to_add}")
print(f"Позиція для вставки (індекс): {pos}")

my_sorted_list.insert(pos, element_to_add)
print(f"Список після вставки: {my_sorted_list}")