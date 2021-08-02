class People:
    """
    class for People object
    """
    def __init__(self, position: list) -> None:
        self.x = int(position[0])
        self.y = int(position[1])
        self.zombie = 0
