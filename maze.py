#cosider X = WALL
# . = FOOD
# O = FOOD BOOST (MORE POINTS)

from layoutConstants import (CELL_SIZE, UI_ROWS,
                             MAZE_START_X,MAZE_START_Y)

maze_level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X............X............X",
    "XOXX....XXXX.X.XXXX....XXOX",
    "X.......X  X.X.X  X.......X",
    "X.XXXX..XXXX.X.XXXX..XXXX.X",
    "X.........................X",
    "X.XXXX.X..XXXXXXX.X..XXXX.X",
    "X......X.....X....X.......X",
    "XXXXXX.XXXXX.X.XXXXX.XXXXXX",
    "X......X.....X.....X......X",
    "X......X...X...X...X......X",
    "X.XXXX.XX.XXXXXXX.XX.XXXX.X",
    "X.........................X",
    "X.XX.X.....XXXXX.....X.XX.X",
    "XOXX.XXX...X.X.X...XXX.XXOX",
    "X......XX..X.X.X..XX......X",
    "X............X............X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

def maze_data(maze):
    walls = []
    food = []
    power_food = []

    for row in range(len(maze)):
        for column in range(len(maze[row])):
            char = maze[row][column]

            char_x = MAZE_START_X + CELL_SIZE * column
            char_y = MAZE_START_Y - CELL_SIZE * row

            if char == "X":
                walls.append((char_x, char_y))
            elif char == ".":
                food.append((char_x, char_y))
            elif char == "O":
                power_food.append((char_x, char_y))

    return walls, food, power_food