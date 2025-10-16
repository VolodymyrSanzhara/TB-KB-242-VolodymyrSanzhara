def sort_phonebook(phonebook):
    """Сортує телефонний довідник за іменем студента."""
    return sorted(phonebook, key=lambda student: student['name'])

def print_phonebook(phonebook):
    """Виводить увесь телефонний довідник."""
    if not phonebook:
        print("Телефонний довідник порожній.")
        return
    print("--------------------------------------------------")
    print("Телефонний довідник:")
    print("--------------------------------------------------")
    for student in phonebook:
        print(f"Ім'я: {student['name']}, Телефон: {student['phone']}, Email: {student['email']}, Група: {student['group']}")
    print("--------------------------------------------------")

def add_student(phonebook):
    """Додає нового студента до довідника."""
    print("--- Додати нового студента ---")
    name = input("Введіть ім'я: ")
    phone = input("Введіть телефон: ")
    email = input("Введіть email: ")
    group = input("Введіть групу: ")
    
    new_student = {
        'name': name,
        'phone': phone,
        'email': email,
        'group': group
    }
    
    phonebook.append(new_student)
    print(f"Студента {name} додано.")
    return sort_phonebook(phonebook)

def delete_student(phonebook):
    """Видаляє студента з довідника."""
    print("--- Видалити студента ---")
    name_to_delete = input("Введіть ім'я студента для видалення: ")
    
    initial_len = len(phonebook)
    phonebook = [student for student in phonebook if student['name'] != name_to_delete]
    
    if len(phonebook) < initial_len:
        print(f"Студента {name_to_delete} видалено.")
    else:
        print(f"Студента з ім'ям {name_to_delete} не знайдено.")
    
    return sort_phonebook(phonebook)

def update_student(phonebook):
    """
    Змінює інформацію про існуючого студента.
    """
    print("--- Змінити дані студента ---")
    name_to_update = input("Введіть ім'я студента, дані якого потрібно змінити: ")
    
    found = False
    for i, student in enumerate(phonebook):
        if student['name'] == name_to_update:
            found = True
            print("Знайдено! Введіть нові дані. Залиште поле порожнім, щоб не змінювати.")
            
            new_phone = input(f"Новий телефон ({student['phone']}): ")
            if new_phone:
                phonebook[i]['phone'] = new_phone
                
            new_email = input(f"Новий email ({student['email']}): ")
            if new_email:
                phonebook[i]['email'] = new_email
                
            new_group = input(f"Нова група ({student['group']}): ")
            if new_group:
                phonebook[i]['group'] = new_group
                
            print(f"Дані студента {name_to_update} оновлено.")
            break
            
    if not found:
        print(f"Студента з ім'ям {name_to_update} не знайдено.")

    return sort_phonebook(phonebook)

def main():
    """Основна функція програми."""
    phonebook = []
    
    while True:
        print("\nВиберіть дію:")
        print("1. Додати нового студента")
        print("2. Змінити дані студента")
        print("3. Видалити студента")
        print("4. Показати весь довідник")
        print("5. Вийти з програми")
        
        choice = input("Ваш вибір: ")
        
        if choice == '1':
            phonebook = add_student(phonebook)
        elif choice == '2':
            phonebook = update_student(phonebook)
        elif choice == '3':
            phonebook = delete_student(phonebook)
        elif choice == '4':
            print_phonebook(phonebook)
        elif choice == '5':
            print("Програма завершує роботу.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()