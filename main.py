import turtle
import pandas
from final_board import Final_board

screen = turtle.Screen()
screen.title("Voivodeships of Poland")
image = "map.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("16_states.csv")
all_states = data.state.to_list()
guessed_states = []

final_board = Final_board()

while len(guessed_states) < 16:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/16 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

while len(guessed_states) == 16:
    final_board.game_over()
    screen.exitonclick()