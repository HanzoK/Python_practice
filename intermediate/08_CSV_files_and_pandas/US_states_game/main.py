import turtle
import pandas
import state_class

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
guessed_states = []

def write_name(guess):
    state_to_be_created = data[data["state"] == f"{guess}"]
    state_x = state_to_be_created.x.item()
    state_y = state_to_be_created.y.item() 
    new_state = state_class.state(guess, state_x, state_y)

game_is_on = True
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"({len(guessed_states)}/50) guessed States", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in guessed_states:
        print("You already guessed that state!")
    elif answer_state in data["state"].values:
        write_name(answer_state)
        guessed_states.append(answer_state)
    else:
        continue

# states_to_learn.csv
# states_to_learn = []
# for item in data["state"]:
#     if item not in guessed_states:
#         states_to_learn.append(item)
states_to_learn = [item for item in data["state"] if item not in guessed_states]
new_csv = pandas.DataFrame(states_to_learn)
new_csv.to_csv("states_to_learn.csv")

