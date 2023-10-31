import turtle
import pandas

screen = turtle.Screen()
data = pandas.read_csv("./50_states.csv")
ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")

# Setup
all_states = data.state.to_list()
all_x_coor = data.x.to_list()
all_y_coor = data.y.to_list()
guessed_states = []
score = 0

screen.title("US States Quiz")
background = "blank_states_img.gif"
screen.addshape(background)
turtle.shape(background)


while len(guessed_states) != 50:
    answer_state = screen.textinput(title=f"{score}/50 States Guessed", prompt="Enter:").title()
    if answer_state == "Exit":
        missing_states = [item for item in all_states if item not in guessed_states]
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("States To Learn.csv")
        break

    for index in range(len(all_states)):
        if (answer_state == all_states[index]) and (answer_state not in guessed_states):
            found = True
            guessed_states.append(answer_state)

            t = turtle.Turtle()
            t.speed(0)
            t.hideturtle()
            t.penup()
            t.goto(all_x_coor[index], all_y_coor[index])
            t.write(answer_state, align=ALIGNMENT, font=FONT)
            score += 1

            break

turtle.mainloop()
