import turtle
import random
from layoutConstants import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, PACMAN_MOVE_SPEED, ENEMY_MOVE_SPEED

class Actor(turtle.Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.speed(0)

    def get_heading(self):
        return round(self.heading())

class Player(Actor):
    def __init__(self, walls):
        super().__init__()

        self.showturtle()
        self.shape("turtle")
        self.shapesize(1.1)
        self.fillcolor("#EBCB73")
        self.pencolor("#EBCB73")

        self.state = "stop"
        self.move_speed = PACMAN_MOVE_SPEED
        self.lives = 3
        self.score = 0
        self.walls = walls

    def move(self):

        if self.state != "stop":
            self.forward(self.move_speed)

        # Top wrap
        if self.ycor() > SCREEN_HEIGHT / 2:
            self.sety(-SCREEN_HEIGHT / 2)

        # Bottom wrap
        elif self.ycor() < -SCREEN_HEIGHT / 2:
            self.sety(SCREEN_HEIGHT / 2)

        # Right wrap
        elif self.xcor() > SCREEN_WIDTH / 2:
            self.setx(-SCREEN_WIDTH / 2)

        # Left wrap
        elif self.xcor() < -SCREEN_WIDTH / 2:
            self.setx(SCREEN_WIDTH / 2)

    def wall_collision(self):
        round_x = round(self.xcor())
        round_y = round(self.ycor())
        heading = self.get_heading()
        half_cell = round(CELL_SIZE / 2)

        for x, y in self.walls:
            dx = round_x - x
            dy = round_y - y

            # Right collision
            if heading == 0:
                if -half_cell < dx + half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x - CELL_SIZE)
                    self.state = "stop"
                elif -half_cell < dx + half_cell < half_cell and dy > half_cell and abs(dy) < CELL_SIZE:
                    self.sety(y + CELL_SIZE)
                elif dy < -half_cell and abs(dy) < CELL_SIZE and -half_cell < dx + half_cell < half_cell:
                    self.sety(y - CELL_SIZE)

            # Left collision
            elif heading == 180:
                if -half_cell < dx - half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x + CELL_SIZE)
                    self.state = "stop"
                elif dy > half_cell and abs(dy) < CELL_SIZE and -half_cell < dx - half_cell < half_cell:
                    self.sety(y + CELL_SIZE)
                elif dy < -half_cell and abs(dy) < CELL_SIZE and -half_cell < dx - half_cell < half_cell:
                    self.sety(y - CELL_SIZE)

            # Up collision
            elif heading == 90:
                if -half_cell <= dx <= half_cell and -half_cell < dy + half_cell < half_cell:
                    self.sety(y - CELL_SIZE)
                    self.state = "stop"
                elif dx > half_cell and abs(dx) < CELL_SIZE and -half_cell < dy + half_cell < half_cell:
                    self.setx(x + CELL_SIZE)
                elif dx < -half_cell and abs(dx) < CELL_SIZE and -half_cell < dy + half_cell < half_cell:
                    self.setx(x - CELL_SIZE)

            # Down collision
            elif heading == 270:
                if -half_cell <= dx <= half_cell and -half_cell < dy - half_cell < half_cell:
                    self.sety(y + CELL_SIZE)
                    self.state = "stop"
                elif dx > half_cell and abs(dx) < CELL_SIZE and -half_cell < dy - half_cell < half_cell:
                    self.setx(x + CELL_SIZE)
                elif dx < -half_cell and abs(dx) < CELL_SIZE and -half_cell < dy - half_cell < half_cell:
                    self.setx(x - CELL_SIZE)

    def move_right(self):
        self.setheading(0)
        self.state = "move"

    def move_left(self):
        self.setheading(180)
        self.state = "move"

    def move_up(self):
        self.setheading(90)
        self.state = "move"

    def move_down(self):
        self.setheading(270)
        self.state = "move"

    def reset_speed(self):
        self.move_speed = PACMAN_MOVE_SPEED  

class Enemy(Actor):
    def __init__(self, walls, start_x, start_y, color):
        super().__init__()

        self.showturtle()
        self.shape("circle")
        self.shapesize(1.2)
        self.fillcolor(color)
        self.pencolor(color)
        self.goto(start_x,start_y)
        self.state = "move"
        self.walls = walls

    def move(self):

        if self.state != "stop":
            self.forward(ENEMY_MOVE_SPEED)

        # Top wrap
        if self.ycor() > SCREEN_HEIGHT / 2:
            self.sety(-SCREEN_HEIGHT / 2)

        # Bottom wrap
        elif self.ycor() < -SCREEN_HEIGHT / 2:
            self.sety(SCREEN_HEIGHT / 2)

        # Right wrap
        elif self.xcor() > SCREEN_WIDTH / 2:
            self.setx(-SCREEN_WIDTH / 2)

        # Left wrap
        elif self.xcor() < -SCREEN_WIDTH / 2:
            self.setx(SCREEN_WIDTH / 2)

    def wall_collision(self):
        round_x = round(self.xcor())
        round_y = round(self.ycor())
        heading = self.get_heading()
        half_cell = round(CELL_SIZE / 2)

        for x, y in self.walls:
            dx = round_x - x
            dy = round_y - y

            # Right collision
            if heading == 0:
                if -half_cell < dx + half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x - CELL_SIZE)
                    self.start_move()
                elif -half_cell < dx + half_cell < half_cell and dy > half_cell and abs(dy) < CELL_SIZE:
                    self.sety(y + CELL_SIZE)
                elif dy < -half_cell and abs(dy) < CELL_SIZE and -half_cell < dx + half_cell < half_cell:
                    self.sety(y - CELL_SIZE)

            # Left collision
            elif heading == 180:
                if -half_cell < dx - half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x + CELL_SIZE)
                    self.start_move()
                elif dy > half_cell and abs(dy) < CELL_SIZE and -half_cell < dx - half_cell < half_cell:
                    self.sety(y + CELL_SIZE)
                elif dy < -half_cell and abs(dy) < CELL_SIZE and -half_cell < dx - half_cell < half_cell:
                    self.sety(y - CELL_SIZE)

            # Up collision
            elif heading == 90:
                if -half_cell <= dx <= half_cell and -half_cell < dy + half_cell < half_cell:
                    self.sety(y - CELL_SIZE)
                    self.start_move()
                elif dx > half_cell and abs(dx) < CELL_SIZE and -half_cell < dy + half_cell < half_cell:
                    self.setx(x + CELL_SIZE)
                elif dx < -half_cell and abs(dx) < CELL_SIZE and -half_cell < dy + half_cell < half_cell:
                    self.setx(x - CELL_SIZE)

            # Down collision
            elif heading == 270:
                if -half_cell <= dx <= half_cell and -half_cell < dy - half_cell < half_cell:
                    self.sety(y + CELL_SIZE)
                    self.start_move()
                elif dx > half_cell and abs(dx) < CELL_SIZE and -half_cell < dy - half_cell < half_cell:
                    self.setx(x + CELL_SIZE)
                elif dx < -half_cell and abs(dx) < CELL_SIZE and -half_cell < dy - half_cell < half_cell:
                    self.setx(x - CELL_SIZE)

    def start_move(self):
        right_cell = (round(self.xcor()) + CELL_SIZE, round(self.ycor()))
        left_cell = (round(self.xcor()) - CELL_SIZE, round(self.ycor()))
        top_cell = (round(self.xcor()), round(self.ycor()) + CELL_SIZE)
        bottom_cell = (round(self.xcor()), round(self.ycor()) - CELL_SIZE)

        next_possible_cell = [right_cell, left_cell, top_cell, bottom_cell]

        for cell in next_possible_cell[:]:
            if cell in self.walls:
                next_possible_cell.remove(cell)

        if not next_possible_cell:
            return

        next_cell = random.choice(next_possible_cell)

        if next_cell == right_cell:
            self.setheading(0)

        elif next_cell == left_cell:
            self.setheading(180)

        elif next_cell == top_cell:
            self.setheading(90)

        elif next_cell == bottom_cell:
            self.setheading(270)
        
        self.state = "move"