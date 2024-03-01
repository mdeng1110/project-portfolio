from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # super().__init__()
        # self.score = 0
        # self.color("white")
        # self.penup()
        # self.goto(0, 270)
        # self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        # self.hideturtle()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
    
    def game_over(self):
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        

      