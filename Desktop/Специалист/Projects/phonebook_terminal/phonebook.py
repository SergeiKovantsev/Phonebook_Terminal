import os

# Файл для хранения данных
data_file = "phonebook.txt"

# Вывод записей постранично
def display_entries(entries, page_size, page_number):
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    for index, entry in enumerate(entries[start_index:end_index], start=start_index + 1):
        print(f"{index}. {entry}")

# Добавляем новую запись
def add_entry(entries):
    surname = input("Фамилия: ")
    name = input("Имя: ")
    patronymic = input("Отчество: ")
    organization = input("Название организации: ")
    work_phone = input("Телефон рабочий: ")
    personal_phone = input("Телефон личный (сотовый): ")

    new_entry = f"{surname},{name},{patronymic},{organization},{work_phone},{personal_phone}"
    entries.append(new_entry)

    with open(data_file, "a") as file:
        file.write(new_entry + "\n")

    print("Запись успешно добавлена!")

# Изменение записи
def edit_entry(entries):
    display_entries(entries, len(entries), 1)

    entry_number = int(input("\nВведите номер записи, которую хотите изменить: "))
    if 1 <= entry_number <= len(entries):
        entry_index = entry_number - 1
        entry = entries[entry_index].split(',')

        print("\nТекущая информация:")
        print(f"1. Фамилия: {entry[0]}")
        print(f"2. Имя: {entry[1]}")
        print(f"3. Отчество: {entry[2]}")
        print(f"4. Название организации: {entry[3]}")
        print(f"5. Телефон рабочий: {entry[4]}")
        print(f"6. Телефон личный (сотовый): {entry[5]}")

        field_number = int(input("\nВыберите номер поля для изменения (или 0 для выхода): "))
        if 1 <= field_number <= 6:
            new_value = input("Введите новое значение: ")
            entry[field_number - 1] = new_value

            entries[entry_index] = ",".join(entry)
            with open(data_file, "w") as file:
                file.write("\n".join(entries))

            print("Запись успешно изменена!")


# Поиск записей
def search_entries(entries):
    search_term = input("Введите текст для поиска: ").lower()
    search_results = []

    for entry in entries:
        if search_term in entry.lower():
            search_results.append(entry)

    if search_results:
        print("\nРезультаты поиска:")
        for result in search_results:
            print(result)
    else:
        print("Записи не найдены.")

# Основная функция
def main():
    entries = []

    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            entries = file.read().splitlines()

    while True:
        print("\n1. Вывод записей")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск записей")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            page_size = 5
            total_entries = len(entries)
            total_pages = (total_entries + page_size - 1) // page_size

            print(f"\nВсего записей: {total_entries}")

            page_number = 1
            while True:
                print(f"\nСтраница {page_number}/{total_pages}")
                display_entries(entries, page_size, page_number)

                print("\n1. Следующая страница")
                print("2. Предыдущая страница")
                print("3. Вернуться в меню")

                page_choice = input("Выберите действие: ")

                if page_choice == "1" and page_number < total_pages:
                    page_number += 1
                elif page_choice == "2" and page_number > 1:
                    page_number -= 1
                elif page_choice == "3":
                    break

        elif choice == "2":
            add_entry(entries)

        elif choice == "3":
            edit_entry(entries)

        elif choice == "4":
            search_entries(entries)

        elif choice == "5":
            break

# Запуск программы
if __name__ == "__main__":
    main()
