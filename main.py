# importing modules
from turtle import Turtle, Screen
import pandas 
# pandas.read_csv() cut

# creating screen
screen = Screen()
screen.title("States of India Quiz")
screen.setup(width=630, height=737)
screen.bgpic("Indian-States-Plotter-main\India-Map.gif")

# extracting data from "Indian-States.csv" file
data = pandas .read_csv("Indian-States-Plotter-main\Indian-States.csv")
states_dict = {row.state:(row.x, row.y) for (index, row) in data.iterrows()}

# some variables to store values
add_guess = 0
answered_states = []

# keep running in the while loop until we input "EXIT" to exit
while True:
    # plotting the states by taking the input
    guessed_state = screen.textinput(f"{add_guess}/{len(states_dict)} states correct", "Enter a state name 👇").upper()
    if guessed_state in states_dict:
        answered_states.append(guessed_state)
        add_guess += 1
        tr = Turtle()
        tr.penup()
        tr.hideturtle()
        tr.goto(states_dict[guessed_state])
        tr.write(guessed_state, align="center", font=('Arial', 8, 'bold'))
        tr.dot(5)

    # creating a csv file of states that we need to learn while exiting
    if guessed_state == "EXIT":
        missing_states = [state for state in states_dict if state not in answered_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Indian-States-Plotter-main\states-to-learn.csv")
        break
