from classes.play_grid import PlayZone


class Zombie(PlayZone):
    """
    class for Zombie object
    """
    def __init__(self, position: list, n: int) -> None:
        super().__init__(n)
        self.x = int(position[0])
        self.y = int(position[1])

    def move(self, direction: str) -> None:
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

