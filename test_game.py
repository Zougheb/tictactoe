import game


board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


def mock_board():
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


def test_display_board():
    assert game.display_board(board) == mock_board()


def test_player_input_with_mark_x(monkeypatch):
    mark = 'x'
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt: mark)
        result = game.player_input()
    assert result == ('X', 'O')


def test_player_input_with_mark_o(monkeypatch):
    mark = 'o'
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt: mark)
        result = game.player_input()
    assert result == ('O', 'X')


def mock_board_after_add_mark():
    print('   |   |')
    print(' ' + board[7] + ' | ' '$' ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def test_place_maker():
    print(mock_board())
    assert game.place_marker(board, '$', 8) == mock_board_after_add_mark()


def test_choose_first():
    pass


def test_space_check():
    pass


def test_player_choice():
    pass


def test_replay_with_yes(monkeypatch):
    answer = 'y'
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt: answer)
        result = game.replay()
    assert not result == 'n'
