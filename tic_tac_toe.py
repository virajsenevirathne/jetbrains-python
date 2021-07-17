def print_field():
    print(f"---------\n"
          f"| {field[0][0]} {field[0][1]} {field[0][2]} |\n"
          f"| {field[1][0]} {field[1][1]} {field[1][2]} |\n"
          f"| {field[2][0]} {field[2][1]} {field[2][2]} |\n"
          f"---------")


def validate_coordinates(inputs):
    """
    Validates coordinates entered by a user
    :param inputs: coordinates
    """
    is_valid = True
    if not (inputs[0].isdigit() and inputs[1].isdigit()):
        print("You should enter numbers!")
        is_valid = False
    elif not (1 <= int(inputs[0]) <= 3 and 1 <= int(inputs[1]) <= 3):
        print("Coordinates should be from 1 to 3!")
        is_valid = False
    elif field[int(inputs[0]) - 1][int(inputs[1]) - 1] != " ":
        print("This cell is occupied! Choose another one!")
        is_valid = False

    return is_valid


def check_winnings():
    """
    Checking all the possible winning combinations.
    :return: 'n' no one, 'X' and 'O' usual meanings
    """
    winning_player = 'n'  # i for impossible, n no one, X and O usual meanings
    for i in range(len(field)):  # vertical win
        if field[0][i] == field[1][i] == field[2][i]:
            winning_player = field[0][i]

    for i in range(len(field)):  # horizontal win
        if field[i][0] == field[i][1] == field[i][2]:
            winning_player = field[i][0]

    if field[0][0] == field[1][1] == field[2][2]:  # Diagonal win
        winning_player = field[1][1]

    if field[0][2] == field[1][1] == field[2][0]:  # Diagonal win
        winning_player = field[1][1]

    return 'n' if winning_player == ' ' else winning_player


def get_input(current_player):
    """
    Get current user input
    :param current_player: sign of the palyer
    """
    while True:
        global field
        coordinates = input("Enter the coordinates: ").split()
        if validate_coordinates(coordinates):
            field[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = current_player
            break


def initialise_field():
    """
    Initialise empty field.
    """
    chars = [" " for _ in range(9)]
    return [chars[i:i + 3] for i in range(0, 9, 3)]


# initialising the field
field = initialise_field()
print_field()

turn = 0

while check_winnings() == 'n' and turn < 9:
    player = "X" if turn % 2 == 0 else "O"
    get_input(player)
    print_field()
    turn += 1
else:
    winner = check_winnings()
    if winner == 'n':
        print("Draw")
    else:
        print(f"{winner} wins")
