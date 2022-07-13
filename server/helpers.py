WINNING_COMBINATIONS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def validate_tic_tac_toe(board):
    for combination in WINNING_COMBINATIONS:
        check = [board[index] for index in combination]
        if check == ['X', 'X', 'X']:
            return 'X'
        if check == ['O', 'O', 'O']:
            return 'O'

    if '' in board:
        return 'continue'
    return 'stalemate'
