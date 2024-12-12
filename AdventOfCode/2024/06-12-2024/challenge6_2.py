'''
--- Part Two ---
While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and record the nightly status of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.

Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get stuck in a loop, making the rest of the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would like to know all of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

In the above example, there are only 6 different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use O to mark the new obstruction, | to show a position where the guard moves up/down, - to show a position where the guard moves left/right, and + to show a position where the guard moves both up/down and left/right.

Option one, put a printing press next to the guard's starting position:

....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...
Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:


....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...
Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...
Option four, put an alchemical retroencabulator near the bottom left corner:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...
Option five, put the alchemical retroencabulator a bit to the right instead:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...
Option six, put a tank of sovereign glue right next to the tank of universal solvent:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..
It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing. The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example, there are 6 different positions you could choose.

You need to get the guard stuck in a loop by adding a single new obstruction. How many different positions could you choose for this obstruction?
'''
def check_overlap_orizontal(direction, matrix, x_guard, y_guard):
    if direction == 'right':
        pass
    else:
        pass
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

def checkTab(counter, x_guard, y_guard, matrix, direction):
    if matrix[x_guard][y_guard] == '.':
        if direction == 'right' or direction == 'left':
            matrix[x_guard][y_guard] = '-'
            counter += check_overlap_orizontal(direction, matrix, x_guard, y_guard)
        if direction == 'up' or direction == 'down':
            matrix[x_guard][y_guard] = '|'    
            counter += check_overlap_orizontal(direction, matrix, x_guard, y_guard)
 
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
    counter_distinc = checkTab(counter_distinc, x_guard, y_guard, matrix, direction)
print(counter_distinc)