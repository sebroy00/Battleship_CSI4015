import random
import time
import random_selection
import hunt_target
import plot

def printBoard(board):
    for x in board:
        print(x)
    print

def empty_board():
    size = 10
    return [[0 for x in range(size)] for y in range(size)] 

def ship_placement_horz(board, ship_len):
    horizontal_ships = []
    row = 0
    while (row < len(board[0])):
        col = 0
        while (col + ship_len <= len(board[0])):
            if board[row][col] == 0:
                ship_horz_positions = [[row, col]] # initial position of ship if places
                build_count = 1
                ship_placed = True
                while (build_count < ship_len):
                    if board[row][col + build_count] != 0:
                        ship_placed = False
                    else:
                        ship_horz_positions.append([row, col+build_count])
                    build_count = build_count+1
                if ship_placed:
                    horizontal_ships.append(ship_horz_positions)
            col = col+1
        row = row+1
    return horizontal_ships


def ship_placement_vert(board, ship_len):
    vertical_ships = []
    col = 0
    while (col < len(board[0])):
        row = 0
        while (row + ship_len <= len(board[0])):
            if board[row][col] == 0:
                ship_vert_positions = [[row, col]] # initial position of ship if places
                build_count = 1
                ship_placed = True
                while (build_count < ship_len):
                    if board[row + build_count][col] != 0:
                        ship_placed = False
                    else:
                        ship_vert_positions.append([row + build_count, col])
                    build_count = build_count+1
                if ship_placed:
                    vertical_ships.append(ship_vert_positions)
            row = row+1
        col = col+1
    return vertical_ships

def ship_placement(board, ship_len):
    horz = ship_placement_horz(board, ship_len)
    vert = ship_placement_vert(board, ship_len)
    
    possible_ship_placements = horz + vert
    
    if len(possible_ship_placements) == 0:
        raise Exception('impossible to add ship', ship_len)
    
    ship_index = random.randint(0,len(possible_ship_placements)-1)
    if len(horz)-1 < ship_index:
        orientation = 0 # horizontal orientation
    else:
        orientation = 1 # vertical orientation
    ship = possible_ship_placements[ship_index]

    board = place_ship_on_board(board, ship, orientation)
    return board

def place_ship_on_board(board, ship, orientation):
    if orientation == 0:
        const_col = ship[0][1]

        first_row = ship[0]
        top_row = first_row[0]-1
        if top_row > -1:
            board[top_row][const_col] = 9  
            if const_col-1 > -1:
                    board[top_row][const_col-1] = 9
            if const_col+1 < len(board[0]):
                    board[top_row][const_col+1] = 9

        for ship_pos in ship:
            cur_row = ship_pos[0]
            board[cur_row][const_col] = len(ship) # place ship numbers
            if const_col-1 > -1:
                board[cur_row][const_col-1] = 9
            if const_col+1 < len(board[0]):
                board[cur_row][const_col+1] = 9

        last_row = ship[len(ship)-1]
        bottom_row = last_row[0]+1
        if bottom_row < len(board[0]):
            board[bottom_row][const_col] = 9  
            if const_col-1 > -1:
                board[bottom_row][const_col-1] = 9
            if const_col+1 < len(board[0]):
                board[bottom_row][const_col+1] = 9
    else:
        const_row = ship[0][0]
        
        first_col = ship[0]
        left_col = first_col[1]-1
        if left_col > -1:
            board[const_row][left_col] = 9  
            if const_row-1 > -1:
                board[const_row-1][left_col] = 9
            if const_row+1 < len(board[0]):
                board[const_row+1][left_col] = 9

        for ship_pos in ship:
            cur_col = ship_pos[1]
            board[const_row][cur_col] = len(ship) # place ship numbers
            if const_row-1 > -1:
                board[const_row-1][cur_col] = 9
            if const_row+1 < len(board[0]):
                board[const_row+1][cur_col] = 9

        last_col = ship[len(ship)-1]
        right_col = last_col[1]+1
        if right_col < len(board[0]):
            board[const_row][right_col] = 9  
            if const_row-1 > -1:
                board[const_row-1][right_col] = 9
            if const_row+1 < len(board[0]):
                board[const_row+1][right_col] = 9

    return board


def build_board():
    board = empty_board()
    try: 
        for ship_len in [5,4,3,2]:
            #print('placing ship of lenght', ship_len)
            board = ship_placement(board, ship_len)
            #printBoard(board)
            #print()
            #printBoard(board)
    except Exception as inst:
        print(inst.args)
        print('reset')
        build_board()
    return board

def create_all_boards(num_boards):
    start = time.clock()
    print('building boards')
    all_boards = []
    for x in range(num_boards):
        board = build_board()
        all_boards.append(board)
    end = time.clock()
    print(end- start)
    return all_boards 
