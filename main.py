from os import getenv


class PlayZone:
    def __init__(self, n: int):
        self.max = n - 1
        self.min = 0

    def try_swap(self, index):
        if index > self.max:
            index = self.min
        elif index < self.min:
            index = self.max
        return index

    def swap_if_needed(self, x, y):
        x = self.try_swap(x)
        y = self.try_swap(y)
        return x, y


class Zombie(PlayZone):
    def __init__(self, position, n):
        super().__init__(n)
        self.x = int(position[0])
        self.y = int(position[1])

    def move(self, direction):
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
    def __init__(self, position):
        self.x = int(position[0])
        self.y = int(position[1])
        self.zombie = 0


def try_infect():
    global zombies_list,peoples_list
    for zombie in zombies_list:
        for people in peoples_list:
            if people.zombie == 1:
                continue
            if zombie.x == people.x and zombie.y == people.y:
                people.zombie = 1
                print(f"Zombie-{zombies_list.index(zombie)} infect human at ({zombie.x},{zombie.y})")

    for people in peoples_list:
        if people.zombie == 1:
            zombies_list.append(Zombie([people.x, people.y], play_zone_size))
            peoples_list.remove(people)



def start_print():
    print("---------------------------------")
    print(f"Map size: {play_zone_size}")

    print("Zombies position:")
    for zombie in zombies_list:
        print(f"Zombie-{zombies_list.index(zombie)} position ({zombie.x},{zombie.y})")
    print("Peoples position:")

    for people in peoples_list:
        print(f"People-{peoples_list.index(people)} position ({people.x},{people.y})")

    if len(peoples_list) == 0:
        print("none")

    print(f"Sequence: {getenv('SEQUENCE')}")
    print("---------------------------------")


def final_print():
    print("---------------------------------")
    print("Zombies position:")
    for zombie in zombies_list:
        print(f"Zombie-{zombies_list.index(zombie)} position ({zombie.x},{zombie.y})")
    print("Peoples position:")

    for people in peoples_list:
        print(f"People-{peoples_list.index(people)} position ({people.x},{people.y})")

    if len(peoples_list) == 0:
        print("none")
    print("---------------------------------")


def check_win(alives):
    if len(alives) == 0:
        final_print()
        return True
    return False


def sequence_queue():
    i = 0
    while True:
        seq = getenv("SEQUENCE")
        if i == len(seq):
            i = 0
        yield seq[i]
        i += 1


def new_game():
    print("START GAME")
    global sequence, game_over, peoples_list, zombies_list
    game_over = False
    sequence = sequence_queue()
    zombies_list = []
    peoples_list = []

    zombies_list.append(Zombie(getenv("ZOMBIE").split(","), play_zone_size))
    people = getenv("PEOPLE").replace("(", "").replace(")", "").split(" ")
    for item in people:
        if item:
            peoples_list.append(People(item.split(",")))
    start_print()


def game():
    global sequence, game_over, peoples_list, zombies_list
    while not game_over:
        for zombie in zombies_list:
            game_over = True
            zombie.move(next(sequence))
            print(f"Zombie-{zombies_list.index(zombie)} go to ({zombie.x},{zombie.y})", flush=True)
        try_infect()
        game_over = check_win(peoples_list)


play_zone_size = int(getenv("PLACESIZE"))
zombies_list = []
peoples_list = []
game_over = False
sequence = {}


if __name__ == '__main__':
    new_game()
    game()
