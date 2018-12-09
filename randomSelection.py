import time
import battleship as bship

boards, ships = bship.create_all_boards()

def play():
    start = time.clock()
    for i in range(len(boards)):
        random_selection(boards[i])
        if (i % 1000 == 0 and i != 0):
            elapsed = (time.clock() - start)
            print 'Number of boards solved', i, 'time: ', elapsed

def random_selection(board):
    a = 0

play()