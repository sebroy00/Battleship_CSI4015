import time
import numpy as np
import random as rnd
import plot as plot

import battleship as bship

def solve(boards, with_parity=False, best_odds=False):
    print('Starting Hunt/Target with parity=', with_parity)
    attempts = []
    start = time.clock()
    for i in range(len(boards)):
        attempts.append(hunt(boards[i], with_parity, best_odds))
        if (i % 1000 == 0 and i != 0):
            elapsed = (time.clock() - start)
            print('Number of boards solved',i,'| time:', elapsed)
    return attempts
    
def all_coordinates(size):
    return [(i, j) for j in range(size) for i in range(size)]

def get_best_odd_coord(coordinates, ship_hit_counts):
    # initialize board with all coordinates as 1
    size = 10
    player_board = [[1 for x in range(size)] for y in range(size)] 
    # set 0 for all coordinates that are still able to hold a ship part
    for (row, column) in coordinates:
        player_board[row][column] = 0

    ship_placements_horz = []
    ship_placements_vert = []
    for i in [0,1,2,3]:
        if ship_hit_counts[i] < 2+i:
            ship_placements_horz += bship.ship_placement_horz(player_board, 2+i)
            ship_placements_vert += bship.ship_placement_vert(player_board, 2+i)

    odds_board = bship.empty_board()
    for horz in ship_placements_horz:
        row = horz[0]
        for col in horz[1]:
            odds_board[row][col] = odds_board[row][col]+1 #increase odds count for each placement

    for vert in ship_placements_vert:
        col = vert[0]
        for row in vert[1]:
            odds_board[row][col] = odds_board[row][col]+1 #increase odds count for each placement

    #bship.printBoard(odds_board)

    # get the coordinates of the maximum 
    max_odd = 0
    selected_coord = (0,0)
    row_count = 0
    for row in odds_board:
        row_max = max(row)
        if row_max > max_odd:
            max_odd = row_max
            selected_coord = (row_count, row.index(max_odd))
        row_count = row_count+1

    #print(max_odd)
    return coordinates.index((selected_coord))

def chose_next_coord(coordinates, with_parity=False, best_odds=False, ship_hit_counts=None):
    if best_odds:
        return get_best_odd_coord(coordinates, ship_hit_counts)
    chosen_coord = rnd.randint(0, len(coordinates)-1)
    if with_parity and chosen_coord % 2 == 0:
        chosen_coord = rnd.randrange(0, len(coordinates), 2)
    return chosen_coord

def hunt(board, with_parity=False, best_odds=False):
    coordinates = all_coordinates(len(board))
    ship_sunk_required = [2,3,4,5]
    ship_hit_counts = [0,0,0,0] # 2,3,4,5
    attempt_count = 0 # number of selections made by player
    print()
    print('current board:')
    bship.printBoard(board)
    print()
    while not np.array_equal(ship_hit_counts, ship_sunk_required) and len(coordinates) > 0:
        print('hit counts', ship_hit_counts)
        print()
        chosen_coord = chose_next_coord(coordinates, with_parity, best_odds, ship_hit_counts)
        (row, column) = coordinates[chosen_coord]
        coordinates.remove(coordinates[chosen_coord])
        for i in [0,1,2,3]:
            if board[row][column] == (2+i):
                attempt_count_target, board, coordinates, ship_hit_counts = target(row, column, board, coordinates, ship_hit_counts, ship_sunk_required)
                attempt_count += attempt_count_target
                ship_hit_counts[i] = ship_hit_counts[i]+1 
        attempt_count = attempt_count+1
    return attempt_count

def target(hit_row, hit_column, board, coordinates, ship_hit_counts, ship_sunk_required):
    left = (hit_row-1, hit_column)
    right = (hit_row+1, hit_column)
    top = (hit_row, hit_column+1)
    bottom = (hit_row, hit_column-1)

    targets = []
    if left in coordinates:
        coordinates.remove(left)
        targets.append(left)
    if right in coordinates:
        coordinates.remove(right)
        targets.append(right)
    if top in coordinates:
        coordinates.remove(top)
        targets.append(top)
    if bottom in coordinates:
        coordinates.remove(bottom)
        targets.append(bottom)
    
    attempt_count_target = 0
    while len(targets) > 0 and not np.array_equal(ship_hit_counts, ship_sunk_required) and len(coordinates) > 0:
        (row, column)= targets.pop()
        for i in [0,1,2,3]:
            if board[row][column] == (2 + i):
                attempt_count_target2, board, coordinates, ship_hit_counts = target(row, column, board, coordinates, ship_hit_counts, ship_sunk_required)
                attempt_count_target += attempt_count_target2
                ship_hit_counts[i] = ship_hit_counts[i] + 1 
        attempt_count_target = attempt_count_target + 1
    return attempt_count_target, board, coordinates, ship_hit_counts