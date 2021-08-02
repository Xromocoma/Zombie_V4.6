import tests
from classes.games import Games

def test_starting_out():
    assert Games() != Exception
