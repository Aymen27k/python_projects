from turtle import Turtle

MOVE_DISTANCE = 20
X_COR = [0, -20, -40]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.is_paused = False

    def _create_segments(self):
        new_tile = Turtle("square")
        new_tile.penup()
        new_tile.color("white")
        return new_tile

    def create_snake(self):
        for tile in range(3):
            new_tile = self._create_segments()
            new_tile.goto(x=X_COR[tile], y=0)
            self.segments.append(new_tile)

    def add_segment(self):
        new_tile = self._create_segments()
        new_tile.goto(self.tail.position())
        self.segments.append(new_tile)

    def moving_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def toggle_pause(self):
        self.is_paused = not self.is_paused

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
