import turtle
import pandas

screen = turtle.Screen()
screen.title("US State game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
should_continue = True
total = 0
data = pandas.read_csv("50_states.csv")
# tim = turtle.Turtle()
index = 0
Guessed_Countries_List = []
countries_missing = []


while should_continue:
    answer = screen.textinput(title=f'Guess the state {total}/50', prompt="What's a state")
    index = 0
    for temp in data.state:
        if answer == "exit":
            should_continue = False
        elif temp in Guessed_Countries_List:
            pass
        elif answer.lower() == temp.lower():
            total += 1
            tim = turtle.Turtle()
            tim.hideturtle()
            tim.penup()
            # Alternative way to line 31
            row_data = data[data.state == temp]
            tim.goto(int(row_data.x), int(row_data.y))
            # tim.goto(data.iat[index, 1], data.iat[index, 2])
            tim.write(f"{temp}")
            Guessed_Countries_List.append(temp)
        else:
            index += 1


#Add the missing states to a list
# for temp in data.state:
#     if temp not in Guessed_Countries_List:
#         countries_missing.append(temp)
countries_missing = [temp for temp in data.state if temp not in Guessed_Countries_List]

output = pandas.DataFrame(countries_missing)
output.to_csv("Countries_missing.csv", index=False)


