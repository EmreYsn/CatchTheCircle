import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("pink")
drawing_board.title("Catch The Circle")
FONT = ('Arial',30,'normal')
score = 0
game_over = False

circle_list = []

score_circle = turtle.Turtle()

countdown_circle = turtle.Turtle()

def setup_turtle_write():
    score_circle.hideturtle()
    score_circle.color("blue")
    score_circle.penup()

    top_height = drawing_board.window_height() / 2
    y = top_height * 0.9
    score_circle.setposition(0,y)
    score_circle.write(arg="Score:0",move=False,align="center",font=FONT)

grid_size = 15

def make_circle(x,y):
    t = turtle.Turtle()
    t.color("red")

    def click_circle(x , y):
        global score
        score += 1
        score_circle.clear()
        score_circle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)


    t.onclick(click_circle)
    t.penup()
    t.shape("circle")
    t.shapesize(2,2)
    t.goto(x * grid_size,y * grid_size)
    circle_list.append(t)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [-20,-10,0,10,20]

def setup_circles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_circle(x,y)

def hide_circles():
    for t in circle_list:
        t.hideturtle()

def show_circles_randomly():
    if not game_over:
        hide_circles()
        random.choice(circle_list).showturtle()
        drawing_board.ontimer(show_circles_randomly, 500)

def countdown(time):
    global game_over
    countdown_circle.hideturtle()
    countdown_circle.color("purple")
    countdown_circle.penup()

    countdown_circle.hideturtle()
    countdown_circle.color("dark blue")
    countdown_circle.penup()

    top_height = drawing_board.window_height() / 2
    y = top_height * 0.9
    countdown_circle.setposition(0,y - 40)
    countdown_circle.clear()

    if time > 0:
        countdown_circle.clear()
        countdown_circle.write(arg="Time: {}".format(time),move=False,align="center",font=(FONT))
        drawing_board.ontimer(lambda: countdown(time - 1), 1000)

    else:
        game_over = True
        countdown_circle.clear()
        hide_circles()
        countdown_circle.write(arg="Game Over!!", move=False, align="center", font=(FONT))

def start_game_up():
    turtle.tracer(0)
    setup_turtle_write()
    setup_circles()
    hide_circles()
    show_circles_randomly()
    countdown(10)
    turtle.tracer(1)

start_game_up()
turtle.mainloop()

