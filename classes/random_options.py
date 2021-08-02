from random import randint, choice
from classes.zombie import Zombie
from classes.people import People


class MakeRandomOptions:
    """
    class for generation random options if choose game_mod - 2
    """

    def __init__(self) -> None:

        self.size = self.random_map_size()
        self.sequence = self.random_sequence()
        self.peoples = self.random_people_list()
        self.zombies = self.random_zombie_list()

    def random_map_size(self) -> int:
        return randint(3, 10)

    def random_sequence(self) -> str:
        seq = ""
        for i in range(randint(4, 8)):
            seq += choice("UDRL")
        return seq

    def random_people_list(self) -> list:
        temp_list = []
        peoples_size = int(self.size / 2) + 1
        for item in range(peoples_size):
            coordinates = self.generate_coordinate(temp_list)
            human = People(coordinates)
            temp_list.append(human)
        return temp_list

    def random_zombie_list(self) -> list:
        return [Zombie(self.generate_coordinate(self.peoples), self.size)]

    def generate_coordinate(self, peoples: list) -> list:
        """
        generate new coordinates for zombie and people
        :param peoples: list - list of all people
        :return: list - coordinates
        """
        while True:
            x = randint(0, self.size - 1)
            y = randint(0, self.size - 1)
            for item in peoples:
                if item:
                    if item.x == x and item.y == y:
                        continue
            break
        return [x, y]
