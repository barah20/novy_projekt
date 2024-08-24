from turtle import Turtle, Screen
import time
import random
import turtle




# Proměnné
score = 0
highest_Score = 0


screen = Screen()
screen.bgcolor("light green")
screen.title("Snake game")
screen.setup(width = 600,height = 600)
screen.tracer(False)

# Hadí hlava
head = Turtle("square")
head.color("black","salmon")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"
# jablko
apple = Turtle("circle")
apple.color("black","red")
apple.penup()
apple.goto(100, 100)
# score 
score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("black")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0,265)
score_sign.write(f"Score: {score}  Highest score: 0", align="center", font=("Arial", 18))
# body parts
body_parts=[]


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# Funkce
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_left():
    if head.direction != "right":
        head.direction = "left"

# Kliknutí na klávesy
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")

# Hlavní cyklus
while True:
    # Kontrola kolize s hranou plátna
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0,0)
        head.direction = "stop"

        # Skryjeme části těla
        for one_bodypart in body_parts:
            one_bodypart.goto(1500,1500)

        # Vyčistíme list s částmi těla
        body_parts.clear()
    # Resetování score
        score = 0
        score_sign.clear()
        score_sign.write(f"Score: {score}  Highest score: {highest_Score}", align="center", font=("Arial", 18))

# Kolize hlavy s jablkem
    if head.distance(apple) < 20:
        x = random.randint(-260,260)
        y = random.randint(-260,260)
        apple.goto(x ,y)
        

    # přidání části těla
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("blue")
        new_body_part.penup()
        body_parts.append(new_body_part)

        # zvýšení score
        score += 1
        if score > highest_Score:
            highest_Score = score
        score_sign.clear()
        score_sign.write(f"Score: {score}  Highest score: {highest_Score}", align="center", font=("Arial", 18))


    for index in range(len(body_parts)-1,0,-1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x,y)


    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)



    move()
    # Hlava narazila do těla
    for one_bodypart in body_parts:
        if one_bodypart.distance(head) < 20:
            time.sleep(2)
            head.goto(0,0)
            head.direction = "stop"
            
            # Skryjeme části těla
            for one_bodypart in body_parts:
             one_bodypart.goto(1500,1500)

            # Vyčistíme list s částmi těla
            body_parts.clear()
            # Resetování score
            score = 0
            score_sign.clear()
            score_sign.write(f"Score: {score}  Highest score: {highest_Score}", align="center", font=("Arial", 18))

  
  
    time.sleep(0.1)
    screen.update()

screen.exitonclick()