# Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.

def move(position, roll):
    return position + 2*roll


print(move(2,5))
