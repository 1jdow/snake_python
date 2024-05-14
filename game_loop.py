import random
import setup


# High score
high_score = 0

# Load the high score if it exists
try:
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    pass

def update_high_score():
    global high_score
    if score > high_score:
        high_score = score
        with open("high_score.txt", "w") as file:
            file.write(str(high_score))

def game_loop():
    setup.stamper.clearstamps()  # Remove existing stamps made by setup.stamper.

    new_head = snake[-1].copy()
    new_head[0] += setup.offsets[snake_direction][0]
    new_head[1] += setup.offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < - setup.WIDTH / 2 or new_head[0] > setup.WIDTH / 2 \
            or new_head[1] < - setup.HEIGHT / 2 or new_head[1] > setup.HEIGHT / 2:
        reset()
    else:
        # Add new head to snake body.
        snake.append(new_head)

        # Check food collision
        if not food_collision():
            snake.pop(0)  # Keep the snake the same length unless fed.

        # Draw snake.
        setup.stamper.shape("assets/snake-head-20x20.gif")
        setup.stamper.goto(snake[-1][0], snake[-1][1])
        setup.stamper.stamp()
        setup.stamper.shape("circle")
        for segment in snake[:-1]:
            setup.stamper.goto(segment[0], segment[1])
            setup.stamper.stamp()

        # Refresh setup.screen
        setup.screen.title(f"Snake Game. Score: {score}. High Score {high_score}")
        setup.screen.update()

        # Rinse and repeat
        setup.turtle.ontimer(game_loop, setup.DELAY)


def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1  # score = score + 1
        update_high_score()
        food_pos = get_random_food_pos()
        setup.food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(- int(setup.WIDTH / 2) + setup.FOOD_SIZE, int(setup.WIDTH / 2) - setup.FOOD_SIZE)
    y = random.randint(- int(setup.HEIGHT / 2) + setup.FOOD_SIZE, int(setup.HEIGHT / 2) - setup.FOOD_SIZE)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Pythagoras' Theorem
    return distance


def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    setup.food.goto(food_pos)
    game_loop()

def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down":  # No self-collision by pressing wrong key.
            snake_direction = "up"
    elif direction == "down":
        if snake_direction != "up":
            snake_direction = "down"
    elif direction == "left":
        if snake_direction != "right":
            snake_direction = "left"
    elif direction == "right":
        if snake_direction != "left":
            snake_direction = "right"

def bind_direction_keys():
    setup.screen.onkey(lambda: set_snake_direction("up"), "Up")
    setup.screen.onkey(lambda: set_snake_direction("down"), "Down")
    setup.screen.onkey(lambda: set_snake_direction("left"), "Left")
    setup.screen.onkey(lambda: set_snake_direction("right"), "Right")

