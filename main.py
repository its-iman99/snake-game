from turtle import Screen
import time
from snake_file import Snake
from food import Food
from scoreboard import Scoreboard

# Screen details
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with wall
    seg_x = snake.segments[0].xcor()
    seg_y = snake.segments[0].ycor()
    if seg_x > 290 or seg_x < -290 or seg_y > 270 or seg_y < -290:
        # game_is_on = False
        score.reset_scoreboard()
        snake.reset()

    # Detect collision with tail
    # for i in range(3, len(snake.segments)):
    #     if snake.segments[0].distance(snake.segments[i]) < 10:
    #         game_is_on = False
    #         score.game_over()

    for segment in snake.segments[3:]:
        if snake.segments[0].distance(segment) < 10:
            # game_is_on = False
            score.reset_scoreboard()
            snake.reset()

    # Detect food intake of snake
    if snake.segments[0].distance(food) < 15:
        points = score.score_track()
        food.refresh()
        snake.extend()

screen.exitonclick()
