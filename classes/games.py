from os import getenv
from func.menu import start_menu
from func.verification import verify_map_size, verify_sequence, verify_coordinates

from classes.file import Logger
from classes.zombie import Zombie
from classes.people import People
from classes.random_options import MakeRandomOptions


class Games:
    def __init__(self):
        self._zombies_list = []
        self._peoples_list = []
        self._map_size = 0
        self._sequence = {}
        self._sequence_string = ""
        self._game_mod = 1
        self._game_over = False

    def _check_win(self) -> None:
        """
        checking for survivors
        """
        if len(self._peoples_list) == 0:
            self._game_over = True
        else:
            self._game_over = False

    def _sequence_queue(self, sequence_str: str) -> iter:
        """
        creating an infinite sequence
        return: generator
        """
        i = 0
        while True:
            seq = sequence_str
            if i == len(seq):
                i = 0
            yield seq[i]
            i += 1

    def _try_infect(self, log) -> None:
        """
        a method of checking if there are zombies and people in one place and then creating a new zombie
        """
        for zombie in self._zombies_list:
            for people in self._peoples_list:
                if people.zombie == 1:
                    continue
                if zombie.x == people.x and zombie.y == people.y:
                    people.zombie = 1
                    log.infect_human(self._zombies_list.index(zombie), zombie.x, zombie.y)

        for people in self._peoples_list:
            if people.zombie == 1:
                self._zombies_list.append(Zombie([people.x, people.y], self._map_size))
                self._peoples_list.remove(people)

    def _init_games(self, log) -> None:
        """
        init new game, create "world"
        """
        log.send_log("START NEW GAME")
        self._game_mod = start_menu(getenv('MOD'))  # Select mod for game
        self._game_over = False
        sequence_string = ""

        if self._game_mod == 1:  # if select manual options
            verify_map_size(getenv("MAP_SIZE"))
            verify_sequence(getenv("SEQUENCE"))

            self._map_size = int(getenv("MAP_SIZE"))
            sequence_string = getenv("SEQUENCE")
            zombie = getenv("ZOMBIE").replace("(", "").replace(")", "").split(" ")
            for item in zombie:
                if item:
                    coordinates = item.split(",")
                    verify_coordinates(coordinates, self._map_size)
                    self._zombies_list.append(Zombie(coordinates, self._map_size))

            if len(self._zombies_list) > 1:
                raise Exception("Invalid count of zombie, you can have only 1 zombie in start")

            peoples = getenv("PEOPLE").replace("(", "").replace(")", "").split(" ")
            for item in peoples:
                if item:
                    coordinates = item.split(",")
                    verify_coordinates(coordinates, self._map_size)
                    self._peoples_list.append(People(coordinates))

        if self._game_mod == 2:  # if select random options
            random_opt = MakeRandomOptions()  # Generate random options

            self._zombies_list = random_opt.zombies
            self._peoples_list = random_opt.peoples
            sequence_string = random_opt.sequence
            self._map_size = random_opt.size

        self._sequence = self._sequence_queue(sequence_string)  # Create infinite sequence
        log.start_print(self._zombies_list, self._peoples_list, self._map_size, sequence_string)

        self._start_games(log)

    def _start_games(self, log) -> None:
        """
        main game loop
        """
        day = 0
        while not self._game_over:
            for zombie in self._zombies_list:  # for each zombie, follow the sequence of moves
                self._game_over = True
                zombie.move(next(self._sequence))
                log.zombie_move(self._zombies_list.index(zombie), zombie.x, zombie.y)

            self._try_infect(log)

            self._check_win()
            day += 1

            if day > 2000000:  # for save memory and stop game if this situation can`t end.
                self._game_over = True

        log.final_print(self._zombies_list, self._peoples_list)  # game end, show result

    def new_game(self):
        try:
            with open("result.txt", "w") as file:  # open file with write access, for create logs
                log = Logger(file)
                self._init_games(log)

            with open("result.txt", "r") as file:  # open file with access, for print all log to console
                print(file.read(), flush=True)

        except Exception as e:
            print("Error:", e)
        finally:
            print("Thanks for using")
