import time
import random as rnd

import numpy as np

def solve(boards):
    print('Starting Random Selection')
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
    # get all possible coordinates on the board
    coordinates = all_coordinates(len(board))
    ship_sunk_counts = [2,3,4,5]
    ship_hit_counts = [0,0,0,0] # ships of length 2,3,4,5
    attempt_count = 0 # number of selections made by player

    # while not all ships are 'sunk' and we still have coordinates to visit
    while not np.array_equal(ship_hit_counts, ship_sunk_counts) and len(coordinates) > 0:
        chosen_coord = rnd.randint(0, len(coordinates)-1)
        (row, column) = coordinates[chosen_coord]
        for i in [0,1,2,3]:
            if board[row][column] == (2 + i):
                ship_hit_counts[i] = ship_hit_counts[i] + 1 
        coordinates.remove(coordinates[chosen_coord])
        attempt_count = attempt_count + 1

    return attempt_count