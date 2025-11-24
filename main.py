from ucs import *

if __name__ == "__main__":
    row = 5
    col = 5
    grid = [
        ['S', '.', '.', '#', '.'],
        ['.', '#', '.', '.', '.'],
        ['.', '.', '.', '#', 'G'],
        ['.', '#', '.', '.', '.'],
        ['.', '.', '.', '.', '.']
    ]
    start = [0, 0]
    goal = [2, 4]

    UCS(row, col, grid, start, goal)


    # for i in range(row):
    #     for j in range(col):
    #         print(grid[i][j], end=' ')
    #     print('\n')