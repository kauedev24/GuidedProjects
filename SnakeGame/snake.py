from turtle import Turtle

"""Configurações iniciais."""
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    
    def create_snake(self):
        """Cria a posição e a quantidade inicial da cobra."""
        for position in STARTING_POSITIONS:
            self.new_snake(position)


    def new_snake(self, position):
        add_snake = Turtle(shape='square')
        add_snake.color('white')
        add_snake.up()
        add_snake.goto(position)
        self.segments.append(add_snake)

    def extend(self):
        self.new_snake(self.segments[-1].position())

    def move(self):
        """Faz a cobra ter movimento contínuo, seguindo o primeiro segmento."""
        for seg_number in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_number-1].xcor()
            new_y = self.segments[seg_number-1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    """Configuração de teclas, definindo o sentido da cobra."""
    def up(self):
        """Norte >> 90°"""
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        """Sul >> 270°"""
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    
    def right(self):
        """Leste >> 0°"""
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        """Oeste >> 180°"""
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

