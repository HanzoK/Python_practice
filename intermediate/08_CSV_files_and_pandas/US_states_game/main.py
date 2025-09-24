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
    state_x = state_to_be_created.x.iloc[0]
    state_y = state_to_be_created.y.iloc[0]
    new_state = state_class.state(answer_state, state_x, state_y)

score = 0
game_is_on = True
while game_is_on:
    if score == 50:
        game_is_on = False
    answer_state = screen.textinput(title=f"Guess the state ({score}/50)", prompt="What's another state's name?").title()
    if answer_state in guessed_states:
        print("You already guessed that state!")
    elif answer_state in data["state"].values:
        write_name(answer_state)
        guessed_states.append(answer_state)
        score += 1
        print(guessed_states)
    else:
        continue
        
screen.exitonclick()