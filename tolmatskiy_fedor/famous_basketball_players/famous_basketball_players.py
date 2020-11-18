LIST_OF_THE_BASKETBALL_PLAYERS = []


def main():
    print(
        "если вы хотите красиво вывести на экран данные всех баскетболистов: введите 1,\n"
        "если хотите добавить игрока: введите 2,\n"
        "если хотите найти данные баскетболиста по имени и фамилии: введите 3,\n"
        "если хотите напечатать данные 3 самых высоких баскетболистов: введите 4,\n"
        "если хотите удалить баскетболиста из списка по имени: введите 5,\n"
        "если хотите остановить ввод напишите: -1\n")
    get_players_info()
    while True:
        func_input = input("Какую функцию вы хотите выполнить? \n")
        if func_input == "1":
            print_all_players()
        elif func_input == "2":
            add_player()
        elif func_input == "3":
            find_player()
        elif func_input == "4":
            high_players()
        elif func_input == "5":
            delete_player()
        elif func_input == "-1":
            save_to_file()
            break


def get_players_info():
    with open("famous_basketball_players.csv") as file:
        lines = file.readlines()
        for line in lines:
            list_of_basketball_info = line.split(",")
            players_info = {
                "first_name": list_of_basketball_info[0],
                "last_name": list_of_basketball_info[1],
                "birth_year": int(list_of_basketball_info[2]),
                "height": int(list_of_basketball_info[3].strip()),
            }
            LIST_OF_THE_BASKETBALL_PLAYERS.append(players_info)
        return LIST_OF_THE_BASKETBALL_PLAYERS


def print_all_players():
    new_keys = {
        "first_name": "Name",
        "last_name": "Last Name",
        "birth_year": "Birth year",
        "height": "Height"
    }
    for player in LIST_OF_THE_BASKETBALL_PLAYERS:
        for key in player:
            print(f'{new_keys[key]}: {player[key]}')


def add_player():
    name = input("Введите имя баскетболиста> ")
    last_name = input("Введите фамилию баскетболиста> ")
    birth_year = input("Введите год рождения баскетболиста> ")
    height = input("Введите рост баскетболиста> ")
    new_player = {
        "first_name": name,
        "last_name": last_name,
        "birth_year": int(birth_year),
        "height": int(height.strip()),
    }
    LIST_OF_THE_BASKETBALL_PLAYERS.append(new_player)
    print(LIST_OF_THE_BASKETBALL_PLAYERS)


def find_player():
    input_find = input("Введите Имя и Фамилию игрока через пробел,которого вы хотите найти> ")
    find = input_find.split()
    for player in LIST_OF_THE_BASKETBALL_PLAYERS:
        if player["first_name"] == find[0] and player["last_name"] == find[1]:
            print(player)


def high_players():
    list_of_height = []
    for player in LIST_OF_THE_BASKETBALL_PLAYERS:
        list_of_height.append(player["height"])
    heights = sorted(list_of_height)[-3:]
    for player in LIST_OF_THE_BASKETBALL_PLAYERS:
        for i in heights:
            if player["height"] == i:
                print(player)


def delete_player():
    input_delete = input("Введите Имя и Фамилию игрока через пробел,которого вы хотите удалить> ")
    delete = input_delete.split()
    for player in LIST_OF_THE_BASKETBALL_PLAYERS:
        if player["first_name"] == delete[0] and player["last_name"] == delete[1]:
            LIST_OF_THE_BASKETBALL_PLAYERS.remove(player)
    print(LIST_OF_THE_BASKETBALL_PLAYERS)


def save_to_file():
    with open("famous_basketball_players.csv", "w") as file:
        n = 0
        list_of_players = []
        for player in LIST_OF_THE_BASKETBALL_PLAYERS:
            for i in list(player.values()):
                i = str(i)
                list_of_players.append(i)
            csv_player_info = ",".join(list_of_players[n:])
            n += 4
            file.write(csv_player_info + "\n")


if __name__ == '__main__':
    main()
