def verify_coordinates(coordinates: list):
    """
    check coordinates for correct input
    :param coordinates: list - x, y coordinates
    """
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if not coordinates:
        raise Exception(f"Illegal parameters for coordinates, check input coordinates and repeat")
    if len(coordinates) != 2 \
        or len(coordinates[0]) > 1 \
        or len(coordinates[1]) > 1 \
        or not coordinates[0].isdigit() \
        or not coordinates[1].isdigit() \
        or int(coordinates[0]) not in num \
        or int(coordinates[1]) not in num:

        raise Exception(f"Illegal parameters for coordinates, check input coordinates and repeat")


def verify_map_size(size: str):
    if not size:
        raise Exception(f"Illegal parameters for grid, check input grid and repeat")
    for item in size:
        if not item.isdigit():
            raise Exception(f"Illegal parameters for grid, check input grid and repeat")
    if int(size) > 100 or int(size) < 2:
        raise Exception(f"Illegal parameters for grid, check input grid and repeat")


def verify_sequence(seq: str):
    success = 'RUDL'
    if not seq:
        raise Exception(f"Illegal parameters for sequence, check input sequence and repeat")
    for item in seq:
        if item not in success:
            raise Exception(f"Illegal parameters for sequence, check input sequence and repeat")