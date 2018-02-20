"""
n queens problem
"""


def is_board_in_legal_state(board):
    for row_1 in range(len(board) - 1):
        for row_2 in range(row_1 + 1, len(board)):
            col_1 = board[row_1] - 1
            col_2 = board[row_2] - 1

            if col_1 == col_2:
                return False

            if abs(row_1 - row_2) == abs(col_1 - col_2):
                return False

    return True


def is_n_queen_solution(n, board):
    return len(board) == n and is_board_in_legal_state(board)


def place_queens(n):
    placements = [[]]
    result = []

    while placements:
        current = placements.pop()
        if is_n_queen_solution(n, current):
            result.append(current)
        for i in range(n, 0, -1):
            new_state = current + [i]

            # pruning
            if len(set(new_state)) != len(new_state):
                continue

            if is_board_in_legal_state(new_state):
                placements.append(new_state)

    return result


# print(is_board_in_legal_state([2, 4, 1, 3]))
# print(is_board_in_legal_state([2, 4, 3, 1]))
# print(is_board_in_legal_state([2, 1, 4, 3]))
# print(is_board_in_legal_state([2, 2]))
# print(is_board_in_legal_state([1]))
# print(is_board_in_legal_state([0, 2, 1]))

print(place_queens(4))
print(place_queens(1))
print(place_queens(2))
print(place_queens(8))
