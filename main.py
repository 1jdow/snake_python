# Import the Turtle Graphics and random modules
import turtle
import game_loop
import setup


setup.screen.listen()
game_loop.bind_direction_keys()

# Set animation in motion
game_loop.reset()

# Finish nicely
turtle.done()
