# Zombie_V4.6 #
## This is simulator of zombie apocalypse
After the nuclear war, a strange and deadly virus has infected the planet producing mindless
zombies. These zombies now wander the world converting any remaining living creatures
they find to zombies as well.

The world is represented by an n x n grid on which zombies and creatures live.
The location of zombies and creatures can be addressed using zero-indexed x-y
coordinates. The top left corner of the world is (x: 0, y: 0). The horizontal coordinate
is represented by x, and the vertical coordinate is represented by y.

At the beginning of the program, a single zombie awakes and begins to move around the
grid following a sequence of movements. Valid movements are Up, Down, Left, Right. The
movement sequence is represented by a string of single character movements, e.g. RDRU
(Right, Down, Right, Up).


## You have 2 different ways to run this project:
### 1 - Run ```python3 ./main.py``` in console

### Before RUN for correct work need install python package ```python-dotenv``` and create .env file
example **.env** file:
```dotenv
SEQUENCE=RDRU
MAP_SIZE=4
ZOMBIE=(3,1)
PEOPLE=(0,1) (1,2) (1,1)
MOD=1  # not required , if you want you can manual input it in project process.
```

### 2 - Use docker-compose to run project
* if you want edit environment you can edit **docker-compose.yml**
and after what

run in console:
``` docker-compose up --build```

rules for environment:


| NAME | TYPE | DESCRIPTION |
|----------------|:---------:|----------------:|
| SEQUENCE | str | sequence of zombie moves, use only ```R D U L``` symbols for sequence
| MAP_SIZE | int | grid size ```MAP_SIZE*MAP_SIZE```  |
| ZOMBIE | str | x,y coordinates of zombie at start, for fill coordinates write ```(x,y)``` where x,y is natural number less then ```MAP_SIZE-1```|
| PEOPLE | str | list of x,y coordinates of people at start, to fill in the coordinates, write the coordinates separated by spaces: ```(x,y) (x1,y1) (x2,y2)``` where x,y is natural number less then ```MAP_SIZE-1```





