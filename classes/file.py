class Logger:
    def __init__(self, input_file):
        self.file = input_file

    def send_log(self, any_string: str):
        self.file.write(f"{any_string}\n")

    def zombie_position(self, name, x, y):
        self.file.write(f"Zombie-{name} position ({x},{y})\n")

    def people_position(self, name, x, y):
        self.file.write(f"People-{name} position ({x},{y})\n")

    def infect_human(self, name, x, y):
        self.file.write(f"Zombie-{name} infect human at ({x},{y})\n")

    def zombie_move(self, name, x, y):
        self.file.write(f"Zombie-{name} go to ({x},{y})\n")

    def start_print(self, zombies_list, peoples_list, map_size, sequence):
        self.send_log("---------------------------------")
        self.send_log(f"Map size: {map_size}")

        self.send_log("Zombies:")
        for zombie in zombies_list:
            self.zombie_position(zombies_list.index(zombie), zombie.x, zombie.y)

        self.send_log("Peoples:")

        for people in peoples_list:
            self.people_position(peoples_list.index(people), people.x, people.y)

        if len(peoples_list) == 0:
            self.send_log("none")

        self.send_log(f"Sequence: {sequence}")
        self.send_log("---------------------------------")

    def final_print(self, zombies_list, peoples_list):
        self.send_log("---------------------------------")
        self.send_log("Zombies:")
        for zombie in zombies_list:
            self.zombie_position(zombies_list.index(zombie), zombie.x, zombie.y)
        self.send_log("Peoples:")

        if len(peoples_list) == 0:
            self.send_log("none")
        else:
            self.send_log("Someone survived ... the zombies lost.")
            for people in peoples_list:
                self.people_position(peoples_list.index(people), people.x, people.y)

        self.send_log("------------END GAME-------------")
        self.send_log("We save log of this game in 'result.txt'")
