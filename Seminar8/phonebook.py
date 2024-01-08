# Задача №49. Общее обсуждение
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# 1) Создать телефонный справочник +
#     - открыть файл в режиме добавления (-a) +
# 2) Добавить контакт +
#     - Запросить информацию у пользователя +
#     - Подготовить данные в необходимом формате +
#     - открыть файл в режиме добавления (-a) +
#     - Добавить контакт в файл +
# 3) Вывести данные из файла: +
#     - открыть файл в режиме чтения +
#     - вывести данные на экран +
# 4) Поиск данных:
#     - Запрос информации у пользователя +
#     - Запрос вариант поиска +
#     - Открыть файл в реежиме чтения (r) +
#     - Сохраниь данные в переменную +
#     - Осуществить поиск по файлу +
#     - Вывести нужную информацию на экран +
# 5) Реализовать UI
#     - Вывести варианты меню +
#     - Получение запроса пользователя +
#     - Реализация запроса пользвоателя +
#     - Выход из программы +


def CreateContact():
    surname = InputSurname()
    name = InputName()
    patronymic = InputPatronymic()
    phone = InputPhone()
    address = InputAddress()
    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'

def AddContact(contact):
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)

def ShowInfo():
    enumedContacts = []
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        allContacts = file.read().rstrip().split('\n\n')
        for nn,contact in enumerate(allContacts,1):
            print(nn,contact)
            enumedContacts.append((nn,contact))
        #print(*enumerate(allContacts,1))
        #print(file.read().rstrip())
        return enumedContacts

def SearchContact():
    varSearch = input("Выберите вариант поиска:\n"
                      "1. По фамилии\n"
                      "2. По имени\n"
                      "3. По отчеству\n"
                      "4. По номеру телефона\n"
                      "5. По адресу\n"
                      "Ввод: ")

    while varSearch not in ('1', '2', '3', '4','5'):
        print("Некорректный ввод данных")
        varSearch = input("Выберите вариант поиска: ")

    indexVar = int(varSearch) - 1
    search = input("Введите данные для поиска: ")
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        allContacts = file.read().rstrip().split('\n\n')
    for contact in allContacts:
        contactlst = contact.replace('\n',' ').split()
        if search in contactlst[indexVar]:
            print(contact)

def CopyContact():
    allContacts = ShowInfo()
    varContact = int(input("Введите номер контакта,который Вы хотите скопировать"))
    #print(allContacts)
    contactToCopy = [x for x in allContacts if x[0] == varContact]
    #print(contactToCopy)
    with open('phonebook_copy.txt', 'a', encoding='UTF-8') as file:
        file.write(contactToCopy[0][1]+"\n\n")
        print("Контакт скопирован")


def InputName():
    return input("Введите имя:")

def InputSurname():
    return input("Введите фамилию:")

def InputPatronymic():
    return input("Введите отчество:")

def InputPhone():
    return input("Введите номер телефона:")

def InputAddress():
    return input("Введите адрес:")




def Interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '5':
        print("##################UltraTurboPhoneBook v1.0.0##################\n"
            "Возможные варинты действий:\n"
            "1) Добавить контакт:\n"
            "2) Вывести на экран\n"
            "3) Поиск контакта\n"
            "4) Копировать контакт в другой файл\n"
            "5) Выход из программы")
        command = input("Выберите пункт меню: ")
        while command not in ('1','2','3','4','5'):
            print("Некорректный ввод данных")
            command = input("Выберите пункт меню: ")
        match command:
            case '1':
                AddContact(CreateContact())
            case '2':
                ShowInfo()
            case '3':
                SearchContact()
            case '4':
                CopyContact()
            case '5':
                print("Программа завершила работу")
                exit(5)
Interface()



