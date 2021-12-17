import sys

board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(9)]

def check(board, x, y):
    vertical = [(x,i) for i in range(9)]
    horizontal = [(i,y) for i in range(9)]
    square = [(i,j) for i in range((x//3)*3, (x//3)*3+3) for j in range((y//3)*3, (y//3)*3+3)]
    check_list = [vertical, horizontal, square]

    temp = [True] * 10

    for l in check_list:
        for nx, ny in l:
            p = board[nx][ny]
            if not p:
                continue
            temp[p] = False

    return temp

def track(board, x, y):
    for i in range(x, 9):
        for j in range(9):
            if i == x and j < y:
                continue
            if i == 8 and j == 8 and board[i][j]:
                for line in board:
                    print(*line, sep="")
                exit(0)
            if board[i][j]:
                continue
            num_list = check(board,i,j)
            for index in range(1,10):
                if not num_list[index]:
                    continue
                board[i][j] = index
                track(board, i, j)
                board[i][j] = 0
            return False

track(board,0,0)