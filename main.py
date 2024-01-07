from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
text = Turtle()
User_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race('red', 'yellow', 'green',"
                                                          " 'blue', 'brown', 'purple')? Enter a color: ")
print(User_bet)
turtle_colors = ["red", "yellow", "green", "blue", "brown", "purple"]
y_axes = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.goto(x=-230, y=y_axes[turtle_index])
    all_turtles.append(new_turtle)

if User_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == User_bet:
                print(f"you've won! The {winning_color} turtle is the winner!")
                text.goto(0, 0)
                text.write("you've won!", align="center", font=("Arial", 15, "normal"))

            else:
                print(f"you've lost! The {winning_color} turtle is the winner!")
                text.goto(0, 0)
                text.write("you've lost!", align="center", font=("Arial", 15, "normal"))

        ran_distance = random.randint(0, 10)
        turtle.forward(ran_distance)


screen.exitonclick()
