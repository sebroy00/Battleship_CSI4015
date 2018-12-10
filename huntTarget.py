import time
import battleship as bship
import numpy as np
import random as rnd
import plot as plot

def solve(boards):
    attempts = []
    start = time.clock()
    for i in range(len(boards)):
        attempts.append(hunt_random(boards[i]))
        if (i % 1000 == 0 and i != 0):
            elapsed = (time.clock() - start)
            print('Number of boards solved',i,'| time:', elapsed)
    return attempts
    
def all_coordinates(size):
    return [(i, j) for j in range(size) for i in range(size)]

def hunt_random(board):
    coordinates = all_coordinates(len(board))
    ship_sunk_required = [2,3,4,5]
    ship_hit_counts = [0,0,0,0] # 2,3,4,5
    attempt_count = 0 # number of selections made by player
    while not np.array_equal(ship_hit_counts, ship_sunk_required) and len(coordinates) > 0:
        chosen_coord = rnd.randint(0, len(coordinates)-1)
        (row, column) = coordinates[chosen_coord]
        coordinates.remove(coordinates[chosen_coord])
        for i in [0,1,2,3]:
            if board[row][column] == (2 + i):
                attempt_count_target, board, coordinates, ship_hit_counts = target(row, column, board, coordinates, ship_hit_counts, ship_sunk_required)
                attempt_count += attempt_count_target
                ship_hit_counts[i] = ship_hit_counts[i] + 1 
        attempt_count = attempt_count + 1
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
