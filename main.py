# Import the turtle and pandas libraries
import turtle
import pandas

# Initialize the score
score = 0

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Set the image for the background map
image = "blank_states_img.gif"
screen.addshape(image)

# Read the CSV file containing state names and their coordinates
data = pandas.read_csv("50_states.csv")

# Create a list of all states from the CSV data
all_states = data.state.to_list()

# Set the turtle shape to the map image
turtle.shape(image)

# Start the game loop
game_is_on = True
while game_is_on:
    # Prompt the user to guess a state
    answer_state = screen.textinput(
        title="Guess the State",
        prompt="What's another State?"
    ).title()  # Capitalize first letter to match data formatting

    # If the user types "Exit", end the game
    if answer_state.lower() == "exit":
        game_is_on = False
        print("Game Over")

    # If the guessed state is correct (exists in the list)
    elif answer_state in all_states:
        # Find the row in the data where the state matches
        state_data = data[data.state == answer_state]

        # Create a new turtle to write the state name on the map
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        # Move the turtle to the state's coordinates
        writer.goto(int(state_data.x), int(state_data.y))
        # Write the name of the state on the map
        writer.write(answer_state)

        # Increase the score and update the window title
        score += 1
        screen.title(f"U.S. States Game - Your score is {score}/50")

# Wait for user click to close the window
screen.exitonclick()


