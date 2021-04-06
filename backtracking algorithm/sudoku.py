board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_qn(qn):
    for i in range(len(qn)):
        if i % 3 == 0 and i != 0:
            print("-----------------------------------")
        for j in range(len(qn[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(qn[i][j])
            else:
                print(str(qn[i][j]) + " ", end=" ")


def find_empty(qn):
    for i in range(len(qn)):
        for j in range(len(qn[0])):
            if qn[i][j] == 0:
                return i, j
    return None


def valid(qn, num, row, col):
    for i in range(len(qn[0])):
        if qn[row][i] == num and col != i:  # row
            return False

    for i in range(len(qn)):
        if qn[i][col] == num and row != i:  # column
            return False

    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if qn[i][j] == num and (i, j) != (row, col):
                return False
    return True


def solve(qn):
    find = find_empty(qn)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(qn, i, row, col):
            qn[row][col] = i

            if solve(qn):
                return True
            qn[row][col] = 0
    return False


print_qn(board)
solve(board)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print_qn(board)
