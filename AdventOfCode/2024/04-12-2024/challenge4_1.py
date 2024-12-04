'''
--- Day 4: Ceres Search ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?

'''

WORD_XMAS = ['X', 'M', 'A', 'S']

def check_xmas_up_vert(i, matrix):
    for c, char in enumerate(WORD_XMAS):
        if char != matrix[i+c]:
            return False
    return True

def check_xmas_down_vert(i, matrix):
    for c, char in enumerate(WORD_XMAS):
        if char != matrix[i-c]:
            return False
    return True

def check_vert_up(i, matrix):
    if i + 3 > 139:
        return 0
    else:
        if check_xmas_up_vert(i, matrix):
            return 1
        else:
            return 0

def check_vert_down(i, matrix):
    if i - 3 < 0:
        return 0
    else:
        if check_xmas_down_vert(i, matrix):
            return 1
        else:
            return 0
            
def check_vert(i, j, matrix):

    ret = 0
    colonna = [row[j] for row in matrix]
    ret += check_vert_up(i, colonna)
    ret += check_vert_down(i, colonna)
    return ret

def check_orizz_right(j , matrix):
    if j + 3 > 139:
        return 0
    else:
        if check_xmas_up_vert(j, matrix):
            return 1
        else:
            return 0

def check_orizz_left(j , matrix):
    if j - 3 < 0:
        return 0
    else:
        if check_xmas_down_vert(j, matrix):
            return 1
        else:
            return 0

def check_orizz(i, j , matrix):

    ret = 0
    ret += check_orizz_right(j ,matrix[i])
    ret += check_orizz_left(j, matrix[i])
    return ret

def check_diag_left_up(i , j, matrix):
    if i -3 < 0 or j -3 < 0:
        return 0 
    else:
        for c, char in enumerate(WORD_XMAS):
            if char != matrix[i-c][j-c]:
                return 0
        return 1

def check_diag_left_down(i , j, matrix):
    if i +3 > 139 or j +3 > 139:
        return 0 
    else:
        for c, char in enumerate(WORD_XMAS):
            if char != matrix[i+c][j+c]:
                return 0
        return 1

def check_diag_left(i , j, matrix):

    ret = 0
    ret += check_diag_left_up(i , j, matrix)
    ret += check_diag_left_down(i , j, matrix)
    return ret

def check_diag_right(i , j, matrix):

    ret = 0
    ret += check_diag_right_up(i , j, matrix)
    ret += check_diag_right_down(i , j, matrix)
    return ret

def check_diag_right_up(i , j, matrix):
    if i +3 > 139 or j -3 < 0:
        return 0 
    else:
        for c, char in enumerate(WORD_XMAS):
            if char != matrix[i+c][j-c]:
                return 0
        return 1
    
def check_diag_right_down(i , j, matrix):
    if j +3 > 139 or i -3 < 0:
        return 0 
    else:
        for c, char in enumerate(WORD_XMAS):
            if char != matrix[i-c][j+c]:
                return 0
        return 1

def count_xmas(matrix):

    counter = 0

    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == 'X':
                counter += check_vert(i, j, matrix)
                counter += check_orizz(i, j, matrix)
                counter += check_diag_left(i , j, matrix)
                counter += check_diag_right(i, j, matrix)

    return counter

input = open("inputpuzzle4.txt", "r")

matrix = []
xmas_counter = 0
for row in input:
    matrix.append(list(row.strip()))
xmas_counter = count_xmas(matrix)

print(xmas_counter)