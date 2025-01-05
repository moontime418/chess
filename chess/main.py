import platform
import os

LINES = {
    0: [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    1: ['1', '♜', '♞', '♝', '♚', '♛', '♝', '♞', '♜'],
    2: ['2', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
    3: ['3', '□', '■', '□', '■', '□', '■', '□', '■'],
    4: ['4', '■', '□', '■', '□', '■', '□', '■', '□'],
    5: ['5', '□', '■', '□', '■', '□', '■', '□', '■'],
    6: ['6', '■', '□', '■', '□', '■', '□', '■', '□'],
    7: ['7', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    8: ['8', '♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
}
WHITE_PIECES = {'♙', '♖', '♘', '♗', '♔', '♕'}
BLACK_PIECES = {'♟', '♜', '♞', '♝', '♚', '♛'}
CHANGE_WHITE = ['♙', '♖', '♘', '♗', '♔']
CHANGE_BLACK = ['♟', '♜', '♞', '♝', '♚']


def init_board():
    return {key: value[:] for key, value in LINES.items()}

def print_board(board):
    for i in range(9):
        print('\t'.join(board[i]))


def is_valid_piece(piece, turn):
    return piece in (WHITE_PIECES if turn % 2 == 0 else BLACK_PIECES)


def reset_cell(board, row, col):
    if row % 2 == 0:
        board[row][col] = '□' if col % 2 == 0 else '■'
    else:
        board[row][col] = '■' if col % 2 == 0 else '□'


def move_pawn(board, start_row, start_col, end_row, end_col, turn):
    player_pieces = CHANGE_WHITE if turn % 2 == 0 else CHANGE_BLACK
    pawn = '♙' if turn % 2 == 0 else '♟'

    if start_col == end_col:
        if abs(start_row - end_row) in (1, 2) and all(
            board[r][start_col] in {'□', '■'} for r in range(min(start_row, end_row) + 1, max(start_row, end_row))
        ):
            board[end_row][end_col] = pawn
            reset_cell(board, start_row, start_col)
            if (turn % 2 == 0 and end_row == 1) or (turn % 2 == 1 and end_row == 8):
                promote_pawn(board, end_row, end_col, player_pieces)
            return True

    elif abs(start_col - end_col) == 1 and abs(start_row - end_row) == 1:
        target_piece = board[end_row][end_col]
        if target_piece in (BLACK_PIECES if turn % 2 == 0 else WHITE_PIECES):
            board[end_row][end_col] = pawn
            reset_cell(board, start_row, start_col)
            return True

    return False


def promote_pawn(board, row, col, player_pieces):
    print("원하는 기물 번호를 선택하세요:")
    for i, piece in enumerate(player_pieces, 1):
        print(f"{i}. {piece}")
    choice = int(input("선택: "))
    board[row][col] = player_pieces[choice - 1]


def player_turn(board, turn):
    while True:
        print("백 차례입니다" if turn % 2 == 0 else "흑 차례입니다")
        start = input("이동할 말을 입력하세요 (예: a2): ")
        start_col, start_row = ord(start[0]) - 96, int(start[1])

        if not is_valid_piece(board[start_row][start_col], turn):
            print("옳지 않은 입력입니다.")
            continue

        end = input("이동할 곳을 입력하세요 (예: a3): ")
        end_col, end_row = ord(end[0]) - 96, int(end[1])

        if board[start_row][start_col] == ('♙' if turn % 2 == 0 else '♟'):
            if move_pawn(board, start_row, start_col, end_row, end_col, turn):
                return

        print("옳지 않은 입력입니다.")


def main():
    board = init_board()
    turn = 0

    while True:
        os.system("cls" if platform.system() == "Windows" else "clear")
        print_board(board)
        player_turn(board, turn)
        turn += 1


if __name__ == "__main__":
    main()
