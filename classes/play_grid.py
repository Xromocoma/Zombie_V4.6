
class PlayZone:
    """
    class for check out from play_zone... but really just show class inheritance
    """

    def __init__(self, n: int) -> None:
        self.max = n - 1
        self.min = 0

    def try_swap(self, index: int) -> int:
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

    def swap_if_needed(self, x: int, y: int) -> (int, int):
        """
        check x and y coordinates
        :param x: int - horizontal coordinate
        :param y: int - vertical coordinate
        :return: x, y - coordinates
        """
        x = self.try_swap(x)
        y = self.try_swap(y)
        return x, y

