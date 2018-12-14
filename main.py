import battleship as bship 
import hunt_target as ht
import random_selection as rs
import plot

boards = bship.create_all_boards(10001)
result1 = ht.solve(boards)
print('best:', min(result1))
result2 = rs.solve(boards)
print('best:', min(result2))
result3 = ht.solve(boards, with_parity=True)
print('best:', min(result3))
result4 = ht.solve(boards, best_odds=True)
print('best:', min(result4))
results = [result1, result2, result3, result4]
group_labels = ['hunt-target', 'random-selection', 'hunt-targer-with-parity', 'hunt-target-odds']
colors = ['#3A4750', '#F64E8B', '#3A4E8B', '#111444']
plot.distribution(results, group_labels, colors)