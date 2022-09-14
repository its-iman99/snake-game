from turtle import Turtle

STARTING_POS = [(0, 0), (20, 0), (40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        posit = self.segments[-1].pos()
        self.add_segment(posit)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[index - 1].xcor()
            y_cor = self.segments[index - 1].ycor()
            self.segments[index].goto(x_cor, y_cor)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        direction = self.segments[0].heading()
        if direction == 0:
            self.segments[0].left(90)
        if direction == 180:
            self.segments[0].right(90)

    def down(self):
        direction = self.segments[0].heading()
        if direction == 0:
            self.segments[0].right(90)
        if direction == 180:
            self.segments[0].left(90)

    def left(self):
        direction = self.segments[0].heading()
        if direction == 90:
            self.segments[0].left(90)
        if direction == 270:
            self.segments[0].right(90)

    def right(self):
        direction = self.segments[0].heading()
        if direction == 90:
            self.segments[0].right(90)
        if direction == 270:
            self.segments[0].left(90)
