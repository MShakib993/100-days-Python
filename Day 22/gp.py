import random

# Computer's random choice: -1 for water, 0 for gun, 1 for snake
computer = random.choice([-1, 0, 1])

# User input: 's' for snake, 'w' for water, 'g' for gun
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

# Mapping from string input to numbers
youdict = {
    "s": 1,   # snake
    "w": -1,  # water
    "g": 0    # gun
}

# Reverse mapping to display choices in output
reversedict = {
    1: "snake",
    -1: "water",
    0: "gun"
}

# Ensure the user's input is valid
if youstr not in youdict:
    print("Invalid input, please choose 's', 'w', or 'g'.")
else:
    # Convert the user's input to the corresponding number
    you = youdict[youstr]

    # Check if it's a draw
    if computer == you:
        print("It's a draw!")
    else:
        # Determine win/lose conditions
        if (computer == 1 and you == -1):  # snake vs water
            print("You lose!")
        elif (computer == -1 and you == 1):  # water vs snake
            print("You win!")
        elif (computer == 1 and you == 0):  # snake vs gun
            print("You win!")
        elif (computer == 0 and you == 1):  # gun vs snake
            print("You lose!")
        elif (computer == -1 and you == 0):  # water vs gun
            print("You lose!")
        elif (computer == 0 and you == -1):  # gun vs water
            print("You win!")

    # Print out the final choices
    print(f"You chose {reversedict[you]}.")
    print(f"Computer chose {reversedict[computer]}.")
