import turtle
from assets import *

# Define program constants
WIDTH = 800
HEIGHT = 600
DELAY = 200  # Milliseconds
FOOD_SIZE = 30

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
screen.bgcolor("yellow")
screen.bgpic("bg2.gif")
screen.register_shape("assets/snake-food-32x32.gif")
screen.register_shape("assets/snake-head-20x20.gif")
screen.tracer(0)  # Turn off automatic animation.



# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("green")
stamper.penup()

# Food
food = turtle.Turtle()
food.shape("assets/snake-food-32x32.gif")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

