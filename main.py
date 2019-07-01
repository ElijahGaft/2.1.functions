# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": ""}, # убрал имя для проверки
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def key_people(key_p):
    num_document = input('Укажите номер документа:')
    for document in documents:
        if document.get("number") == num_document:
            name = document.get("name")
            print('Документ связан с именем {}'.format(name))
            return
        if document == documents[-1]:
            print('Такого документа не существует')


def key_list(key_l):
    print('Вот список документов:')
    for document in documents:
        document_data = list(document.values())
        for data in document_data:
            print('"{}"'.format(data), end=' ')
        print('\n')
    return


def key_shelf(key_s):
    num_document = input('Укажите номер документа:')
    for key_directory in directories:
        for val_directory in directories.get(key_directory):
            if val_directory == num_document:
                print('Документ под номером {} лежит на {} полке'.format(num_document, key_directory))
                return
                # не работает для пустых полок, можно конечно на прямую задать:
                # if val_directory == '' -> лежит на 3й полке


def key_add(key_a):
    while True:
        try:
            type_doc = str(input('Тип документа: '))
            num_doc = input('Номер документа: ')
            name = str(input('ФИО владельца документа: '))
            directory = input('На какую полку положить: ')
            break
        except:
            print('Ошибка формата данных')
    try:
        documents.append({"type": type_doc, "number": num_doc, "name": name})
        for key_directory in directories:
            if directory == key_directory:
                print(type(num_doc))
                directories.get(directory).append(num_doc)
                print(directories)
                return
        directory_new = {directory: list()}
        (directory_new.get(directory)).append(num_doc)
        directories.update(directory_new)
        print(directories)
    except:
        print(
            'Ошибка, ввода. Данные не добавлены')  # чтобы если происходит ошибка не получилось так что какие-то данные внесли, а какие-то нет.

    return


def key_help():
    print('Вот список доступных команд:\n p \n l\n s\n a\n n - новая функция выводящая имена\n help\n exit\n')
    return

def key_name(key_n):
    for document in documents:
        try:
            if document.get("name") != '':
                 print(document.get("name"))
            else:
                raise KeyError
        except KeyError:
            print('Документ с номером', document.get("number"), 'без имени!')
def witch_key(input_key):
    if input_key == 'p':
        key_people(input_key)
        return
    if input_key == 'l':
        key_list(input_key)
        return
    if input_key == 's':
        key_shelf(input_key)
        return
    if input_key == 'n':
        key_name(input_key)
        return
    if input_key == 'a':
        key_add(input_key)
        return
    if input_key == 'help':
        key_help()
        return
    else:
        print('Такой команды не существует.')
        key_help()


def main():
    while True:
        key_input = input('\nВведите команду:')
        if key_input == "exit":
            print('Выхожу из программы')
            return
        else:
            witch_key(key_input)


main()
