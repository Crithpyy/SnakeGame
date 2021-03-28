import turtle
import time
import random

delay=0.1

# Set up screen
win = turtle.Screen()
win.title("Snake game")
win.bgcolor("green")
win.setup(width=600, height=600)
win.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0, 100)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.5, 0.5)
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "bold"))

# Define coordinates
def move():
    if head.direction == "up":
        y = head.ycor()  # y Coordinate of the turtle
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()  # y Coordinate of the turtle
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()  # x Coordinate of the turtle
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()  # x Coordinate of the turtle
        head.setx(x - 20)

# Define movement rules
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

# Listen to keyboard input
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_right, "d")
win.onkeypress(go_left, "a")

# main game loop
while True:
    win.update()

    # check for collision with wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # hide  the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # clear segment list
        segments.clear()


    # Check for collision with the food
    if head.distance(food) <20:
        # Move food to a random new position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        
        # Add a new segment to turtle body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
    
    # move the end segment (in this case: the newly added part of the snakes boy) in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    #check for body collisions
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            segments.clear()

    time.sleep(delay)

wn.mainloop()
