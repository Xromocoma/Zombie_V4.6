from os import getenv
from file import Logger
from menu import start_menu
from random import randint, choice
from verification import verify_map_size, verify_sequence, verify_coordinates

zombies_list = []
peoples_list = []
map_size = 0
sequence_string = ""
game_over = False
sequence = {}


class MakeRandomOptions:
    """
    class for generation random options if choose game_mod - 2
    """

    def __init__(self):
        global zombies_list, peoples_list, sequence_string, map_size
        self.map_size = self.random_map_size()
        self.sequence_string = self.random_sequence()
        self.peoples_list = self.random_people_list()
        self.zombies_list = self.random_zombie_list()

        map_size = self.map_size
        sequence_string = self.sequence_string
        peoples_list = self.peoples_list
        zombies_list = self.zombies_list

    def random_map_size(self) -> int:
        return randint(3, 10)

    def random_sequence(self):
        seq = ""
        for i in range(randint(4, 8)):
            seq += choice("UDRL")
        return seq

    def random_people_list(self):
        temp_list = []
        peoples_size = int(self.map_size / 2) + 1
        for item in range(peoples_size):
            coordinates = self.generate_coordinate(temp_list)
            human = People(coordinates)
            temp_list.append(human)
        return temp_list

    def random_zombie_list(self):
        return [Zombie(self.generate_coordinate(self.peoples_list), self.map_size)]

    def generate_coordinate(self, peoples: list):
        """
        generate new coordinates for zombie and people
        :param peoples: list - list of all people
        :return: list - coordinates
        """
        while True:
            x = randint(0, self.map_size - 1)
            y = randint(0, self.map_size - 1)
            for item in peoples:
                if item:
                    if item.x == x and item.y == y:
                        continue
            break
        return [x, y]


class PlayZone:
    """
    class for check out from play_zone... but really just show class inheritance
    """

    def __init__(self, n: int):
        self.max = n - 1
        self.min = 0

    def try_swap(self, index: int):
        """
        check and jump to the other side if the zombie left the map
        :param index: int - x or y coordinate
        :return: index:int
        """
        if index > self.max:
            index = self.min
        elif index < self.min:
            index = self.max
        return index

    def swap_if_needed(self, x: int, y: int):
        """
        check x and y coordinates
        :param x: int - horizontal coordinate
        :param y: int - vertical coordinate
        :return: x, y - coordinates
        """
        x = self.try_swap(x)
        y = self.try_swap(y)
        return x, y


class Zombie(PlayZone):
    """
    class for Zombie object
    """

    def __init__(self, position: list, n: int):
        super().__init__(n)
        self.x = int(position[0])
        self.y = int(position[1])

    def move(self, direction: str):
        """
        move zombie
        :param direction: str - move direction (R,U,D,L)
        """
        if direction == "R":
            self.x += 1
        elif direction == "D":
            self.y += 1
        elif direction == "U":
            self.y -= 1
        elif direction == "L":
            self.x -= 1

        self.x, self.y = self.swap_if_needed(self.x, self.y)


class People:
    """
    class for People object
    """

    def __init__(self, position: list):
        self.x = int(position[0])
        self.y = int(position[1])
        self.zombie = 0


def try_infect():
    """
    a method of checking if there are zombies and people in one place and then creating a new zombie
    """
    global zombies_list, peoples_list
    for zombie in zombies_list:
        for people in peoples_list:
            if people.zombie == 1:
                continue
            if zombie.x == people.x and zombie.y == people.y:
                people.zombie = 1
                log.infect_human(zombies_list.index(zombie), zombie.x, zombie.y)

    for people in peoples_list:
        if people.zombie == 1:
            zombies_list.append(Zombie([people.x, people.y], map_size))
            peoples_list.remove(people)


def check_win(alive: list):
    """
    :param alive: list of survives
    :return: bool
    """
    if len(alive) == 0:
        return True
    return False


def sequence_queue():
    """
    creating an endless sequence
    """
    i = 0
    while True:
        seq = sequence_string
        if i == len(seq):
            i = 0
        yield seq[i]
        i += 1




def new_game():
    """
    init new game, create "world"
    """
    log.send_log("START NEW GAME")
    global sequence, sequence_string, game_over, peoples_list, zombies_list, map_size
    game_over = False

    if game_mode == 1:  # if select manual options
        verify_map_size(getenv("MAP_SIZE"))
        verify_sequence(getenv("SEQUENCE"))

        map_size = int(getenv("MAP_SIZE"))
        sequence_string = getenv("SEQUENCE")
        zombie = getenv("ZOMBIE").replace("(", "").replace(")", "").split(" ")
        for item in zombie:
            if item:
                coordinates = item.split(",")
                verify_coordinates(coordinates)
                zombies_list.append(Zombie(coordinates, map_size))

        peoples = getenv("PEOPLE").replace("(", "").replace(")", "").split(" ")
        for item in peoples:
            if item:
                coordinates = item.split(",")
                verify_coordinates(coordinates)
                peoples_list.append(People(coordinates))
    if game_mode == 2:  # if select random options
        MakeRandomOptions()

    sequence = sequence_queue()
    log.start_print(zombies_list, peoples_list, map_size, sequence_string)


def game():
    """
    main game loop
    """
    global sequence, game_over, peoples_list, zombies_list
    new_game()
    day = 0
    while not game_over:
        for zombie in zombies_list:  # for each zombie, follow the sequence of moves
            game_over = True
            zombie.move(next(sequence))
            log.zombie_move(zombies_list.index(zombie), zombie.x, zombie.y)

        try_infect()
        game_over = check_win(peoples_list)
        day += 1

        if day > 2000000:  # for save memory and stop game if this situation can`t end.
            game_over = True

    log.final_print(zombies_list, peoples_list)  # game end, show result


if __name__ == '__main__':
    try:
        game_mode = start_menu()
        with open("result.txt", "w") as file:  # open file with write access, for create logs
            log = Logger(file)
            game()

        with open("result.txt", "r") as file:  # open file with access, for print all log to console
            print(file.read(), flush=True)
    except Exception as e:
        print("Error:", e)
    finally:
        print("Thanks for using")
