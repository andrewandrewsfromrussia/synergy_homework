
master_dict = {'Bo': {'type': 'собака', 'old': 5, 'master_name': 'Sten'}, 'Vooo': {'type': 'кот', 'old': 2, 'master_name': 'Djo'}}

def create():
    name = input("Введите имя питомца: ")
    type = input("Введите вид и породу питомца: ")
    old = int(input("Введите возраст питомца: "))
    master_name = input("Введите имя хозяина: ")
    master_dict[name] = {"type": type, "old": old, "master_name": master_name}
    print(master_dict)

def edit():
    print("Вы находитесь в меню редактирования учетной записи.")
    name_d = input('Введите имя питомца, чью учетную запись вы хотите отредактировать: ')
    if name_d in master_dict:
        type = input("Введите вид и породу питомца: ")
        old = int(input("Введите возраст питомца: "))
        master_name = input("Введите имя хозяина: ")
        master_dict[name_d] = {"type": type, "old": old, "master_name": master_name}
        print("Запись успешно отредактирована.")
    else:
        print("Учетная запись не найдена.")
    main()

def delete():
    del_name = input('Введите имя учетной записи для удаления:')
    if input(f"Вы действительно хотите удалить учетную запись {del_name}? y/n: ") == "y":
        del master_dict[del_name]
    else:
        main()

def read():
    for key in master_dict:
        if master_dict[key]["old"] == (1, 21, 31):
            x = 'год'
        elif master_dict[key]["old"] in (2, 3, 4, 22, 23, 24):
            x = 'года'
        elif master_dict[key]["old"] in (
                5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30):
            x = 'лет'
        print(f"{key} - это {master_dict[key]["type"]} возрастом {master_dict[key]["old"]} {x}, чей хозяин {master_dict[key]["master_name"]}")
    main()

def help():
    print("Список команд:")
    print("create - создать учетную запись.")
    print("edit - изменить учетную запись.")
    print("read - список учетных записей.")
    print("del - удалить учетную запись.")
    print("stop - закончить работу.")

def main():
    comm = ""
    while comm != 'stop':
        comm = input('Введите команду (help - список команд): ')
        if comm == 'create':
            if input('Вы хотите создать новую учетную запись? y/n: ') == "y":
                create()
            main()
        elif comm == "edit":
            if input('Вы хотите изменить существующую запись? y/n: ') == "y":
                edit()
            main()
        elif comm == "read":
            read()
        elif comm == "del":
            delete()
        elif comm == "stop":
            exit()
        elif comm == "help":
            help()
        else:
            print("Неверная команда.")
            help()

main()