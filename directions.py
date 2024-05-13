import setup 
import game_loop

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


def bind_direction_keys():
    setup.screen.onkey(lambda: game_loop.set_snake_direction("up"), "Up")
    setup.screen.onkey(lambda: game_loop.set_snake_direction("down"), "Down")
    setup.screen.onkey(lambda: game_loop.set_snake_direction("left"), "Left")
    setup.screen.onkey(lambda: game_loop.set_snake_direction("right"), "Right")
