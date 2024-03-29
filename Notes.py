import json
import datetime
import os

# Создание заметки в формате JSON
def create_note():
    note_title = input("Введите заголовок заметки: ")
    note_content = input("Введите текст заметки: ")
    creator_name = input("Введите фамилию лица, создающего заметку: ")

    if any(char.isdigit() for char in creator_name):
        print("Ошибка: Фамилия не может содержать цифры. Введите текстовый формат.")
        return

    note_id = str(datetime.datetime.now().timestamp())[:3]
    creation_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")  # Получение текущей даты и времени

    note_data = {
        "id": note_id,
        "title": note_title,
        "content": note_content,
        "creator": creator_name,
        "creation_date": creation_date
    }

    with open(f"{note_id}_{note_title}.json", "w") as file:
        json.dump(note_data, file, indent=4)
    
    print(f"Заметка '{note_title}' с id '{note_id}', создана {creation_date} пользователем {creator_name}.")

# Сохранение заметки
def save_note():
    note_id = input("Введите id заметки для сохранения: ")
    updated_content = input("Введите обновленное содержимое заметки: ")
    new_creator_name = input("Введите новую фамилию лица, создающего заметку: ")

    while True:
        try:
            with open(f"{note_id}.json", "r") as file:
                note_data = json.load(file)
            break
        except FileNotFoundError:
            print(f"Ошибка: Заметка с id '{note_id}' не найдена. Введите корректный id.")

    if "content" not in note_data or "creator" not in note_data:
        print("Ошибка: Нельзя сохранить заметку, которая еще не создана.")
        return

    if note_data["content"] == updated_content and note_data["creator"] == new_creator_name:
        print("Ошибка: Нельзя сохранить заметку без изменений.")
        return

    note_data["content"] = updated_content
    note_data["creator"] = new_creator_name

    with open(f"{note_id}.json", "w") as file:
        json.dump(note_data, file, indent=4)

    print(f"Заметка с id '{note_id}' сохранена. Новый создатель: {new_creator_name}")

# Редактирование заметки
def edit_note():
    note_id = input("Введите id заметки для редактирования: ")
    new_content = input("Введите новое содержимое заметки: ")
    new_creator_name = input("Введите новую фамилию лица, создающего заметку: ")

    while True:
        try:
            with open(f"{note_id}.json", "r") as file:
                note_data = json.load(file)
            break
        except FileNotFoundError:
            print(f"Ошибка: Заметка с id '{note_id}' не найдена. Введите корректный идентификатор.")

    if "content" not in note_data or "creator" not in note_data:
        print("Ошибка: Нельзя редактировать несуществующую заметку.")
        return

    if note_data["content"] == new_content and note_data["creator"] == new_creator_name:
        print("Ошибка: Нельзя изменить заметку без изменений.")
        return

    note_data["content"] = new_content
    note_data["creator"] = new_creator_name

    with open(f"{note_id}.json", "w") as file:
        json.dump(note_data, file, indent=4)

    print(f"Заметка с id '{note_id}' отредактирована. Новый создатель: {new_creator_name}")

# Удаление заметки
def delete_note():
    note_id = input("Введите id заметки для удаления: ")

    while True:
        try:
            os.remove(f"{note_id}.json")
            print(f"Заметка с id '{note_id}' удалена.")
            break
        except FileNotFoundError:
            print(f"Ошибка: Заметка с id '{note_id}' не найдена. Введите корректный id.")

# Запрос команды с консоли
while True:
    command = input("Введите команду (create, save, edit, delete) или 'exit' для выхода: ")

    if command == 'create':
        create_note()
    elif command == 'save':
        save_note()
    elif command == 'edit':
        edit_note()
    elif command == 'delete':
        delete_note()
    elif command == 'exit':
        break
    else:
        print("Некорректная команда. Введите одну из доступных команд.")