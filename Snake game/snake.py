from turtle import Turtle
starting_positions = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self) :
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)
            
    def add_segment(self,position):
        new_segment = Turtle()
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
            
    def extend(self):
        self.add_segment(self.segments[-1].position())
            
            
            
            
    """moving the snake foward using the following steps.
But turning the snake has a different story"""
# Simple moving - moving the segments individually
# For Turning - we have to make every piece follow
#               the one ahead of it and move the
#                head as it is.
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            x_cor = self.segments[seg_num-1].xcor()
            y_cor = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x_cor,y_cor)
            self.segments[seg_num].setheading(self.head.heading())
        self.head.forward(20)         # no w for loop is used to get the pieces follow the predecessor and first piece always move ahead by 20 coordinates using the while loop

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)