class MapLink:

    def __init__(self):
        self.map = {}

    def addlink(self, shortlink, link):
        self.map[shortlink] = link
        print("Добавлено\n")

    def isSLink(self, shortlink):
        return shortlink in self.map

    def getLink(self, shortlink):
        return self.map.get(shortlink, None)

    def printShortLinks(self):
        if not self.map:
            print("Хранилище пусто\n")
            return
        for key, value in self.map.items():
            print(f"{key} -> {value}")
        print()

    def deleteLink(self, shortlink):
        if self.isSLink(shortlink):
            del self.map[shortlink]
            return True
        return False

if __name__ == "__main__":
    map = MapLink()

    print("Выберите, что хотите сделать с ссылками и их короткими кодами\n")
    print("1. Добавить ссылку и короткий код на нее\n")
    print("2. Проверить существует ли короткий код\n")
    print("3. Получить ссылку по короткому коду\n")
    print("4. Вывести все короткие коды\n")
    print("5. Удалить ссылку по короткому коду\n")
    print("Все остальные значения - конец работы программы\n")

    A = True
    while A == True:
        vubor = input("")

        match vubor:
            case "1":
                print("Введите длинную ссылку\n")
                l = input("")
                print("Введите короткий код\n")
                sl = input("")

                map.addlink(sl, l)

            case "2":
                print("Введите короткий код\n")
                sl = input("")
                if map.isSLink(sl):
                    print("Существует\n")
                else:
                    print("Отсутствует\n")

            case "3":
                print("Введите короткий код\n")
                sl = input("")
                l = map.getLink(sl)
                if l == None:
                    print("Такой нет\n")
                else:
                    print(f"Итог - {l}\n")

            case "4":
                map.printShortLinks()

            case "5":  # Наша новая кнопка удаления
                print("Введите короткий код для удаления\n")
                sl = input("")
                if map.deleteLink(sl):
                    print("Успешно удалено\n")
                else:
                    print("Такого кода не существовало\n")

            case _:
                print("До встречи!")
                A = False
