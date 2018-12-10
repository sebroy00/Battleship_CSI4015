import random
import time
import randomSelection
import huntTarget
import plot

def printBoard(board):
    for x in board:
        print(x)
    print

def empty_board():
    size = 10 # default
    return [[0 for x in range(size)] for y in range(size)] 

def ship_placement_horz(board, ship_len):
    horizontal_ships = []
    row = 0
    while (row < len(board[0])):
        col = 0
        while (col + ship_len <= len(board[0])):
            if board[row][col] == 0:
                ship_horz_positions = [col] # initial position of ship if places
                build_count = 1
                ship_placed = True
                while (build_count < ship_len):
                    if board[row][col + build_count] != 0:
                        #print(y, x + build_count)
                        ship_placed = False
                    else:
                        ship_horz_positions.append(col + build_count)
                    build_count = build_count + 1
                if ship_placed:
                    horizontal_ships.append([row,ship_horz_positions])
            col = col + 1
        row = row + 1
    return horizontal_ships


def ship_placement_vert(board, ship_len):
    vertical_ships = []
    col = 0
    while (col < len(board[0])):
        row = 0
        while (row + ship_len <= len(board[0])):
            if board[row][col] == 0:
                ship_vert_positions = [row] # initial position of ship if places
                build_count = 1
                ship_placed = True
                while (build_count < ship_len):
                    if board[row + build_count][col] != 0:
                        ship_placed = False
                    else:
                        ship_vert_positions.append(row + build_count)
                    build_count = build_count + 1
                if ship_placed:
                    vertical_ships.append([col,ship_vert_positions])
            row = row + 1
        col = col + 1
    return vertical_ships

def ship_placement(board, ship_len):
    possible_horz_ships = ship_placement_horz(board, ship_len)
    possible_vert_ships = ship_placement_vert(board, ship_len)
    
    if len(possible_horz_ships) != 0 and len(possible_vert_ships) != 0: # both possible
        orientation = random.randint(0,1) # 0 is vertical, 1 is horizontal
    elif len(possible_horz_ships) != 0: # only horizontal possible
        orientation = 1
    elif len(possible_vert_ships) != 0: # only vertical possible
        orientation = 0
    else:
        raise Exception('impossible to add ship', ship_len)
    
    positions = []
    if orientation == 0:
        positions = possible_vert_ships[random.randint(0,len(possible_vert_ships)-1)]
    else:
        positions = possible_horz_ships[random.randint(0,len(possible_horz_ships)-1)]
    
    board = place_ship_on_board(board, orientation, positions)
    
    return board

def place_ship_on_board(board, orientation, positions):
    if orientation == 0:
        const_col = positions[0]
        ship_row = positions[1]
        
        top_row = ship_row[0]-1
        if top_row > -1:
            board[top_row][const_col] = 9  
            if const_col-1 > -1:
                    board[top_row][const_col-1] = 9
            if const_col+1 < len(board[0]):
                    board[top_row][const_col+1] = 9

        for row in ship_row:
            board[row][const_col] = len(ship_row)
            if const_col-1 > -1:
                board[row][const_col-1] = 9
            if const_col+1 < len(board[0]):
                board[row][const_col+1] = 9

        bottom_row = ship_row[len(ship_row)-1]+1
        if bottom_row < len(board[0]):
            board[bottom_row][const_col] = 9  
            if const_col-1 > -1:
                board[bottom_row][const_col-1] = 9
            if const_col+1 < len(board[0]):
                board[bottom_row][const_col+1] = 9
    else:
        const_row = positions[0]
        ship_col = positions[1]

        left_col = ship_col[0]-1
        if left_col > -1:
            board[const_row][left_col] = 9  
            if const_row-1 > -1:
                board[const_row-1][left_col] = 9
            if const_row+1 < len(board[0]):
                board[const_row+1][left_col] = 9

        for col in ship_col:
            board[const_row][col] = len(ship_col)
            if const_row-1 > -1:
                board[const_row-1][col] = 9
            if const_row+1 < len(board[0]):
                board[const_row+1][col] = 9

        right_col = ship_col[len(ship_col)-1]+1
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
    except Exception as inst:
        print(inst.args)
        print('reset')
        build_board()
    return board

def create_all_boards():
    start = time.clock()
    print('building boards')
    all_boards = []
    for x in range(10001):
        board = build_board()
        all_boards.append(board)
    end = time.clock()
    print(end- start)
    return all_boards 


boards = create_all_boards()
result1 = huntTarget.solve(boards)
result2 = randomSelection.solve(boards)
results = [result1, result2]
group_labels = ['hunt-target', 'random-selection']
colors = ['#3A4750', '#F64E8B']
plot.distribution(results, group_labels, colors)