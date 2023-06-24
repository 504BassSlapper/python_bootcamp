import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
all_responses = []

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)
while len(all_responses) < len(all_states):
    answer = screen.textinput(
        title=f"{len(all_responses)}/50 Correct", prompt="What is the state name"
    )
    if answer is None:
        # show response
        full_answer = [x for x in all_states if x not in all_responses]
        print(full_answer)
        for state in full_answer:
            t.color("red")
            state_data = data[data.state == state]
            state_x_coor = int(state_data.x.iloc[0])
            state_y_coor = int(state_data.y.iloc[0])
            t.goto(state_x_coor, state_y_coor)
            t.write(state, align="center")
        break
    answer = answer.title()
    if answer in all_states:
        state_data = data[data.state == answer]
        print(state_data)
        state_x_coor = state_data["x"]
        state_y_coor = state_data["y"]
        t.goto(int(state_x_coor.iloc[0]), int(state_y_coor.iloc[0]))
        t.write(answer, align="center")
        all_responses.append(answer)

t.color("black")
t.goto(0, 280)
t.write(
    f"Game Over\nyour score is {len(all_responses)}/50 ",
    align="center",
    font=("Arial", 12, "bold"),
)

turtle.mainloop()
