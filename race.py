from turtle import *
from random import randint

screen = Screen()
screen.title('Ninja Turtles Race')


def reached_end(raph: Turtle, don: Turtle, mich: Turtle, leo: Turtle) -> bool:
    if raph.xcor() >= 300:
        print("Raphael wins!")
        return True
    elif don.xcor() >= 300:
        print("Donatello wins!")
        return True
    elif mich.xcor() >= 300:
        print("Michelango wins!")
        return True
    elif leo.xcor() >= 300:
        print("Leonardo wins!")
        return True
    return False


def creating_turtles() -> None:

    raphael = Turtle(shape='turtle', visible=False)
    raphael.color('red')
    raphael.penup()
    raphael.goto(-160, 10)
    raphael.pendown()
    raphael.showturtle()

    michelangelo = Turtle(shape='turtle', visible=False)
    michelangelo.color('orange')
    michelangelo.penup()
    michelangelo.goto(-160, 40)
    michelangelo.pendown()
    michelangelo.showturtle()

    leonardo = Turtle(shape='turtle', visible=False)
    leonardo.color('blue')
    leonardo.penup()
    leonardo.goto(-160, 70)
    leonardo.pendown()
    leonardo.showturtle()

    donatello = Turtle(shape='turtle', visible=False)
    donatello.color('purple')
    donatello.penup()
    donatello.goto(-160, 100)
    donatello.pendown()
    donatello.showturtle()

    turtles_race(raphael, donatello, michelangelo, leonardo)


def reset_turtle(turt: Turtle) -> None:
    turt.clear()
    turt.hideturtle()


def turtles_race(raphael: Turtle, donatello: Turtle, michelangelo: Turtle,
                 leonardo: Turtle) -> None:

    while not reached_end(raphael, donatello, michelangelo, leonardo):
        raphael.forward(randint(1, 5))
        donatello.forward(randint(1, 5))
        leonardo.forward(randint(1, 5))
        michelangelo.forward(randint(1, 5))

    reset_turtle(raphael)
    reset_turtle(leonardo)
    reset_turtle(michelangelo)
    reset_turtle(donatello)


while True:
    creating_turtles()
