# Write your code here
import random

STATUS_PLAYER = "player"
STATUS_COMPUTER = "computer"
status = "unknown"
stock_pieces = []
player_pieces = []
computer_pieces = []
domino_snake = [[-1, -1]]


def initialise_game():
    """
    Function to shuffle the pieces among players.
    :return:
    """
    global stock_pieces, player_pieces, computer_pieces, domino_snake, status

    while status == "unknown":
        stock_pieces = []
        player_pieces = []
        computer_pieces = []
        domino_snake = [[-1, -1]]

        for i in range(7):
            for j in range(i, 7):
                stock_pieces.append([i, j])

        for _ in range(7):
            player_piece = stock_pieces.pop(random.randint(0, len(stock_pieces) - 1))
            computer_piece = stock_pieces.pop(random.randint(0, len(stock_pieces) - 1))

            player_pieces.append(player_piece)
            computer_pieces.append(computer_piece)

            if player_piece[0] == player_piece[1] and domino_snake[0][0] < player_piece[0]:
                domino_snake[0] = player_piece
                status = STATUS_COMPUTER
            if computer_piece[0] == computer_piece[1] and domino_snake[0][0] < computer_piece[0]:
                domino_snake[0] = computer_piece
                status = STATUS_PLAYER
    if status == STATUS_COMPUTER:
        player_pieces.remove(domino_snake[0])
    else:
        computer_pieces.remove(domino_snake[0])


def is_valid_output(player_action):
    """
    Check if user input is valid and if valid make changes to hands.
    :param player_action: what piece player want to move
    :return: True if it is a valid move
    """
    global player_pieces, computer_pieces, domino_snake, status
    validity = False
    pieces = player_pieces if status == STATUS_PLAYER else computer_pieces
    item = pieces[abs(player_action) - 1]
    if player_action == 0:
        if len(stock_pieces) > 0:
            pieces.append(stock_pieces.pop(random.randint(0, len(stock_pieces) - 1)))
        validity = True
    elif (player_action < 0 and (domino_snake[0][0] == item[0] or domino_snake[0][0] == item[1])) or (
            player_action > 0 and (domino_snake[-1][1] == item[0] or domino_snake[-1][1] == item[1])):
        validity = True
        piece = pieces.pop(abs(player_action) - 1)
        if player_action < 0:
            if domino_snake[0][0] == item[1]:
                domino_snake.insert(0, piece)
            else:
                domino_snake.insert(0, piece[::-1])
        else:
            if domino_snake[-1][1] == item[0]:
                domino_snake.append(piece)
            else:
                domino_snake.append(piece[::-1])
    if validity:
        status = STATUS_COMPUTER if status == STATUS_PLAYER else STATUS_PLAYER
    return validity


def get_input():
    """
    Function to take input from the player. It also calculates move of the computer as well.
    """
    print_status()

    if status == STATUS_COMPUTER:
        input("\nStatus: Computer is about to make a move. Press Enter to continue...\n")
        computer_pieces_rank = best_item_to_play()
        for i in range(len(computer_pieces_rank)):
            if is_valid_output(computer_pieces_rank[i][0]+1):
                break
            elif is_valid_output(-computer_pieces_rank[i][0]-1):
                break
        else:
            is_valid_output(0)
    else:
        number = input("\nStatus: It's your turn to make a move. Enter your command.\n")
        while True:
            if number.lstrip('-').isdigit() and abs(int(number)) <= len(player_pieces):
                if is_valid_output(int(number)):
                    break
                else:
                    number = input("Illegal move. Please try again.\n")
            else:
                number = input("Invalid input. Please try again..\n")


def print_status():
    """
    Helper function to print the output
    """
    print("======================================================================")
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}")
    print(print_domino_snake())
    print("Your pieces:")
    for i in range(len(player_pieces)):
        print(f"{i + 1}:{str(player_pieces[i])}")


def best_item_to_play():
    """
    Calculates the frequecies of the numbers and return score of each piece in the computer hand.
    :return: sorted list which contain score for each piece in the computer hand
    """
    combined_list = domino_snake + computer_pieces

    # Calculate frequencies
    frequencies = [0] * 7
    for i in range(len(combined_list)):
        for j in range(2):
            frequencies[combined_list[i][j]] += 1

    # Calculate Score
    score_list = [(i, computer_pieces[i], frequencies[computer_pieces[i][0]] + frequencies[computer_pieces[i][1]])
                  for i in range(len(computer_pieces))]
    # sort based in score
    return sorted(score_list, key=lambda x: x[2], reverse=True)


def print_domino_snake():
    """
    Helper function to print the domino snake.
    """
    if len(domino_snake) < 7:
        return f"\n{''.join(str(i) for i in domino_snake)}\n"
    else:
        return f"\n{''.join(str(i) for i in domino_snake[0:3])}...{''.join(str(i) for i in domino_snake[-3:])}\n"


def check_outcome():
    """
    Check the outcome of the game and print the outcome if game is concluded.
    :return: True if game conculded
    """
    outcome = False
    if len(player_pieces) == 0:
        print_status()
        print("\nStatus: The game is over. You won!")
        outcome = True
    elif len(computer_pieces) == 0:
        print_status()
        print("\nStatus: The game is over. The computer won!")
        outcome = True
    elif len(domino_snake) > 3 and domino_snake[0][0] == domino_snake[-1][0]:
        count = 0
        number = domino_snake[0][0]
        for i in range(len(domino_snake)):
            for j in range(2):
                if domino_snake[i][j] == number:
                    count += 1
        if count >= 8:
            print_status()
            print("\nStatus: The game is over. It's a draw!")
            outcome = True

    return outcome


initialise_game()

while True:
    get_input()
    if check_outcome():
        break
