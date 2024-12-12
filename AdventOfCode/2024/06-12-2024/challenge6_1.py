'''
--- Day 6: Guard Gallivant ---
The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.
Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?
'''

def checkwall(direction, x, y, matrix):
    if direction == 'up':
        if matrix[x-1][y] == '#':
            return 'right'
    if direction == 'down':
        if matrix[x+1][y] == '#':
            return 'left'
    if direction == 'left':
        if matrix[x][y-1] == '#':
            return 'up'
    if direction == 'right':
        if matrix[x][y+1] == '#':
            return 'down'
    return direction

def MoveGuard(x_guard, y_guard, matrix, direction):

    direction = checkwall(direction, x_guard, y_guard, matrix)
    if direction == 'up':
        x_guard -= 1
    elif direction == 'down':
        x_guard += 1   
    elif direction == 'right':
        y_guard += 1   
    elif direction == 'left':
        y_guard -= 1    
    return x_guard, y_guard, direction

def checkTab(counter, x_guard, y_guard, matrix):
    if matrix[x_guard][y_guard] == '.':
        counter += 1
        matrix[x_guard][y_guard] = 'x'

    return counter

def checkPositionGuard(x, y, w, h):
    if (x > 0 and x+1 < w) and (y > 0 and y+1 < h):
        return True
    return False

map = open("inputpuzzle6.txt", "r")
matrix = []
x_guard, y_guard = 0,0
for i, row in enumerate(map):
    line = list(row.strip())
    matrix.append(line)
    if '^' in line:
        x_guard = i
        y_guard = line.index('^')

widht, height = len(matrix), len(matrix[0])
matrix[x_guard][y_guard] = 'x'
counter_distinc = 1
outside_map = False
direction = 'up'

while checkPositionGuard(x_guard, y_guard, widht, height):
    x_guard, y_guard, direction = MoveGuard(x_guard, y_guard, matrix, direction)
    counter_distinc = checkTab(counter_distinc, x_guard, y_guard, matrix)
print(counter_distinc)