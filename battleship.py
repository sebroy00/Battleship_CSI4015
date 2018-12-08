def printBoard(board):
    for x in board:
        print(x)

def empty_board():
    size = 5 # default
    return [[0 for x in range(size)] for y in range(size)] 

def ship_placement_horz(board, ship_len):
    horizontal_ships = []
    y = 0
    while (y < len(board[0])):
        x = 0
        while (x + ship_len <= len(board)):
            if board[y][x] == 0:
                ship_horz_positions = [x] # initial position of ship if places
                build_count = 1
                ship_placed = True
                while (build_count < ship_len):
                    if(board[y][x + build_count] != 0):
                        ship_placed = False
                    else:
                        ship_horz_positions.append(x + build_count)
                    build_count = build_count + 1
                if ship_placed:
                    horizontal_ships.append([y,ship_horz_positions])
            x = x + 1
        y = y + 1
    printBoard(board)
    print(horizontal_ships)


def ship_placement_vert(board, ship_len):
    vertical_ships = []
    x = 0
    while (x < len(board[0])):
        y = 0
        while (y + ship_len <= len(board)):
            if board[y][x] == 0:
                ship_horz_positions = [y] # initial position of ship if places
                build_count = 1
                ship_placed = True
                while (build_count < ship_len):
                    if(board[y + build_count][x] != 0):
                        ship_placed = False
                    else:
                        ship_horz_positions.append(y + build_count)
                    build_count = build_count + 1
                if ship_placed:
                    vertical_ships.append([x,ship_horz_positions])
            y = y + 1
        x = x + 1
    printBoard(board)
    print(vertical_ships)

board = empty_board()
for a in range(len(board)):
    board[a][0] = 's'
ship_placement_horz(board, 3)
ship_placement_vert(board, 3)