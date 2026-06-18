#Hello ^ ^ I created pacman using turtle but its in Strawberry matcha cozy theme!!
#To start the game you only need to run the main.py file
#MAKE SURE ALL THE OTHER FILES ARE ALSO IN THE SAME FOLDER AS MAIN.PY

#Hope Y'all enjoy this version!! ^ ^ 

import turtle
import random
from layoutConstants import SCREEN_HEIGHT, SCREEN_WIDTH, CELL_SIZE
from gamescreen import Wall, Food, PowerFood, UiPen
from chars import Player, Enemy


#Creates and sets up the game window
def init_screen():
    screen = turtle.Screen()

    #automatic screen updates is turned off for smoother gameplay
    screen.tracer(0)

    screen.title("Pacman but its matcha")

    screen.setup(SCREEN_WIDTH  , SCREEN_HEIGHT)

    screen.bgcolor("#F4F6F0")

    return screen

def bind_controls(screen, char):
    screen.listen()

    screen.onkey(char.move_right, "Right")
    screen.onkey(char.move_left, "Left")
    screen.onkey(char.move_up, "Up")
    screen.onkey(char.move_down, "Down")

#Updates the screen each frame
def game_loop(screen, char, scores_pen, lives_pen, message_pen, food_pen, power_pen, char_start_x, char_start_y, enemy1, enemy2, enemy3, enemy4 ):
    
    scores_pen.write_score(char.score)
    lives_pen.write_lives(char.lives)

    #points calculation
    for (px, py), stamp_id in list(food_pen.stamps.items()):
        if char.distance(px,py) < CELL_SIZE/2 and (px,py) != (char_start_x,char_start_y):
            food_pen.clearstamp(stamp_id)
            del food_pen.stamps[(px,py)]
            char.score += 5
        elif char.distance(px,py) < CELL_SIZE/2 and (px,py) == (char_start_x,char_start_y):
            food_pen.clearstamp(stamp_id)
            del food_pen.stamps[(px,py)]

    for (px, py), stamp_id in list(power_pen.stamps.items()):
        if char.distance(px,py) < CELL_SIZE/2:
            power_pen.clearstamp(stamp_id)
            del power_pen.stamps[(px,py)]
            char.score += 50
            char.move_speed += 2
            screen.ontimer(char.reset_speed, 3000)
            message_pen.write_message("Congrats! You added a strawberry to your Matcha Latte! ✧｡٩(ˊᗜˋ )و✧*｡")

            screen.ontimer(message_pen.clear_message, 2000)

    # Win condition
    if not food_pen.stamps and not power_pen.stamps:

        screen.clear()

        win_pen = turtle.Turtle()
        win_pen.hideturtle()
        win_pen.penup()

        win_pen.goto(0, 50)
        win_pen.write("🍓 STRAWBERRY MATCHA COMPLETE 🍵",align="center",font=("Courier", 40, "bold"))

        win_pen.goto(0, 0)
        win_pen.write(f"Final Score: {char.score}",align="center",font=("Courier", 20, "bold"))

        win_pen.goto(0, -20)
        win_pen.write("All the matcha powders have been gathered! 🍵",align="center",font=("Courier", 14, "normal"))

        win_pen.goto(0, -45)
        win_pen.write("Your strawberries are ready for a cozy Strawberry Matcha! 🍓",align="center",font=("Courier", 14, "normal"))

        restart_pen = turtle.Turtle()
        restart_pen.hideturtle()
        restart_pen.penup()

        restart_pen.goto(0, -100)
        restart_pen.write("Better brew another Matcha Run! 🍵🍓",align="center",font=("Courier", 24, "bold"))

        def restart_click(x, y):
            if -120 < x < 120 and -110 < y < -50:
                restart_game()

        screen.onclick(restart_click)

        screen.update()
        return

    char.move()
    char.wall_collision()

    enemy1.move()
    enemy1.wall_collision()

    enemy2.move()
    enemy2.wall_collision()

    enemy3.move()
    enemy3.wall_collision()

    enemy4.move()
    enemy4.wall_collision()

    # Enemy collision
    for enemy in [enemy1, enemy2, enemy3, enemy4]:
        if char.distance(enemy) < CELL_SIZE / 2:
            char.lives -= 1

            if char.lives <= 0:

                screen.clear()

                game_over_pen = turtle.Turtle()
                game_over_pen.hideturtle()
                game_over_pen.penup()

                game_over_pen.goto(0, 50)
                game_over_pen.write("GAME OVER",align="center",font=("Courier", 40, "bold"))

                game_over_pen.goto(0, 0)
                game_over_pen.write(f"Final Score: {char.score}",align="center",font=("Courier", 20, "bold"))

                restart_pen = turtle.Turtle()
                restart_pen.hideturtle()
                restart_pen.penup()

                restart_pen.goto(0, -80)
                restart_pen.write("🍓 Restart 🍓 //error fix later:3 ",align="center",font=("Courier", 24, "bold"))

                def restart_click(x, y):
                    if -120 < x < 120 and -110 < y < -50:
                        restart_game()

                screen.onclick(restart_click)

                screen.update()
                return
        
            char.goto(char_start_x, char_start_y)
            char.state = "stop"

            break

    screen.update()
    screen.ontimer(lambda: game_loop(screen,char,scores_pen, lives_pen, message_pen, food_pen, power_pen , char_start_x, char_start_y, enemy1, enemy2, enemy3, enemy4), 1000//60 )

def restart_game():
    turtle.bye()  
    main()        

def main():
    screen = init_screen()

    #create the walls food etc
    wall_pen = Wall()
    food_pen = Food()
    power_pen = PowerFood()
    ui_pen = UiPen()
    scores_pen = UiPen()
    lives_pen = UiPen()
    message_pen = UiPen()

    wall_pen.draw()
    walls = wall_pen.walls

    # Enemy spawn positions 
    enemy1 = Enemy(walls, -120, 120, "#D98B9A")  
    enemy2 = Enemy(walls, 120, 120, "#EAB8C4")   
    enemy3 = Enemy(walls, -120, -120, "#A8C7BE") 
    enemy4 = Enemy(walls, 120, -120, "#DDB899") 

    food_pen.draw()
    power_pen.draw()
    enemy1.showturtle()
    enemy2.showturtle()
    enemy3.showturtle()
    enemy4.showturtle()
    ui_pen.draw_ui_area()

    char_start_coor = random.choice(food_pen.food)
    char_start_x = char_start_coor[0]
    char_start_y = char_start_coor[1]

    char = Player(walls)
    char.goto(char_start_x,char_start_y)



    bind_controls(screen,char)

    game_loop(screen, char,
          scores_pen, lives_pen,message_pen,
          food_pen, power_pen,
          char_start_x, char_start_y,
          enemy1, enemy2, enemy3, enemy4)

    screen.mainloop()

#so the game will run only when this file is executed directly
if __name__ == "__main__":
    main()
