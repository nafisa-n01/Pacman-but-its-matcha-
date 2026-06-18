# All static objects of the gamescreen will be rendered here

import turtle
from maze import maze_data, maze_level_1
from layoutConstants import CELL_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH



class Pen(turtle.Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.color("#384C2F")
        self.speed(0)

        self.walls, self.food, self.power_food = maze_data(maze_level_1)


class Wall(Pen):

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.shapesize(1.2, 1.2)

        self.pencolor("#5A6E62")
        self.fillcolor("#5A6E62")

    def draw(self):
        for x, y in self.walls:
            self.goto(x, y)
            self.stamp()


class Food(Pen):

    def __init__(self):
        super().__init__()
        
        #strechted triangle to make it look similar to a leaf
        self.shape("circle")
        self.shapesize(0.3, 0.4)

        # Matcha leaf color
        self.pencolor("#799567")
        self.fillcolor("#799567")
        self.stamps = {}

    def draw(self):
        for x, y in self.food:
            self.goto(x, y)
            stamp_id = self.stamp()

            self.stamps[(x,y)] = stamp_id


class PowerFood(Pen):

    def __init__(self):
        super().__init__()

        #this is the closest I could to get to a strawberry shape
        self.shape("turtle")
        self.shapesize(0.8, 0.8)
        self.stamps = {}

        self.pencolor("#D87A8C")
        self.fillcolor("#D87A8C")

    def draw(self):
        for x, y in self.power_food:
            self.goto(x, y)
            stamp_id = self.stamp()
            
            self.stamps[(x, y)] = stamp_id

class UiPen(Pen):
    def __init__(self):
        super().__init__()
        self.font = ("Courier", 22, "bold")
    
    def draw_ui_area(self):
        self.penup()

        y = SCREEN_HEIGHT / 2 - CELL_SIZE * 2.5

        self.goto(-SCREEN_WIDTH / 2 + 20, y)
        self.pendown()
        self.goto(SCREEN_WIDTH / 2 - 20, y)

        self.penup()

    def write_score(self,score):
        self.clear()

        msg = f"Score: {score}"
        self.goto(-SCREEN_WIDTH/4, SCREEN_HEIGHT/2 - 2.5*CELL_SIZE)
        self.write(msg, False, "left", self.font)

    def write_lives(self,lives):
        self.clear()

        msg = f"Lives: {lives}"
        self.goto(SCREEN_WIDTH/4, SCREEN_HEIGHT/2 - 2.5*CELL_SIZE)
        self.write(msg, False, "right", self.font)

    def write_message(self, msg):
        self.clear()

        self.goto(0, -330)

        self.write(msg,align="center",font=("Courier", 14, "bold"))

    def clear_message(self):
        self.clear()