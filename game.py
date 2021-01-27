import random


def display_board(board):
    """
    This function prints the board with empty spaces for the user
    :param board: 10 empty spaces
    :return: the board
    """
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    """
    This function prompt the user to choose what mark they want to use
    :return: a tuple of the marks (x , o) based on the user choice
    """
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    """
    This function places the user's mark to the chosen position on the board
    :param board:
    :param marker:
    :param position:
    :return: the user's marker
    """
    board[position] = marker
    return marker


def win_check(board, mark):
    """
    This function check the win cases on the board
    :param board:
    :param mark:
    :return: wining cases
    """
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    """
    This function choose randomly which player should go first
    :return: the chosen player
    """
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    """
    This function checks if the there is a free space on the board for the player to move to
    :param board: the board
    :param position: the position to check if it's free
    :return: True if it's empty
    """
    return board[position] == ' '


def full_board_check(board):
    """
    This function checks if the game is tie by checking if the board is full
    :param board:
    :return: boolean Value (True if full, False otherwise)
    """
    if board.count(' ') > 1:
        return False
    else:
        return True


def player_choice(board):
    """
    This function asks for a player's next position (as a number 1-9) and then uses the space_check function
    to check if its a free position. If it is, then return the position for later use
    :param board:
    :return: the position
    """
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position


def replay():
    """
    this function asks the user if they want to play again
    :return: boolean True if they do want to play again
    """
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


def run_game():
    """
    This is the entry point to run the above functions
    :return:
    """
    print('Welcome to Tic Tac Toe!')
    # winner = None
    player1_wins = 0
    player2_wins = 0

    while True:
        # Reset the board
        the_board = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')

        play_game = input('Are you ready to play? Enter Yes or No.')

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            # game_on = False
            print('No worries! come back whenever you are ready :)')
            break

        while game_on:
            if turn == 'Player 1':
                # Player1's turn.

                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)

                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    player1_wins = player1_wins + 1
                    print(f'player 1 {player1_marker} have won the game!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.

                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    player2_wins = player2_wins + 1
                    print(f'Player 2 {player2_marker} has won!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'

        print(f"player 1: {player1_wins}  points!")
        print(f"player 2 :  {player2_wins} points!")

        if not replay():
            print("hope you enjoyed it!")
            break

        if input("Reset score (y/n): ") == "y":
            player1_wins = 0
            player2_wins = 0


if __name__ == "__main__":
    run_game()
