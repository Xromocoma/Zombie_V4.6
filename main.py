from os import path
from dotenv import load_dotenv
from classes.games import Games


dotenv_path = path.join(path.dirname(__file__), '.env')
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)


if __name__ == '__main__':
    Games().new_game()


