from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed(10)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.x_cord = x_cord
        self.setposition(x_cord, 0)

    def go_up(self):
        new_ycor = self.ycor() + 20
        self.sety(new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - 20
        self.sety(new_ycor)

