if __name__ == "__main__":
    links = {}
    print("1. Добавить | 2. Проверить код | 3. Получить ссылку | 4. Вывести все | 5. Удалить | Другое - Выход\n")

    while True:
        match input("Выберите действие: "):
            case "1":
                url = input("Введите длинную ссылку: ")
                code = input("Введите короткий код: ")
                links[code] = url
                print("Добавлено\n")

            case "2":
                print("Существует\n" if input("Введите короткий код: ") in links else "Отсутствует\n")

            case "3":
                code = input("Введите короткий код: ")
                print(f"Итог - {links[code]}\n" if code in links else "Такой нет\n")

            case "4":
                if not links: print("Хранилище пусто")
                for k, v in links.items(): print(f"{k} -> {v}")
                print()

            case "5":
                print("Успешно удалено\n" if links.pop(input("Введите короткий код для удаления: "), None) else "Такого кода не существовало\n")

            case _:
                print("До встречи!")
                break
