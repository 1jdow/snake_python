import turtle
from assets import *

# Define program constants
WIDTH = 800
HEIGHT = 600
DELAY = 200  # Milliseconds
FOOD_SIZE = 32
SNAKE_SIZE = 20


offsets = {
    "up": (0, SNAKE_SIZE),
    "down": (0, -SNAKE_SIZE),
    "left": (-SNAKE_SIZE, 0),
    "right": (SNAKE_SIZE, 0)
}

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
screen.bgpic("assets/bg2.gif")
screen.register_shape("assets/snake-food-32x32.gif")
screen.register_shape("assets/snake-head-20x20.gif")
screen.tracer(0)  # Turn off automatic animation.



# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("#009ef1")
stamper.penup()

# Food
food = turtle.Turtle()
food.shape("assets/snake-food-32x32.gif")
food.shapesize(FOOD_SIZE / 20)
food.penup()

