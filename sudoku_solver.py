import numpy as np

grid = []

for i in range(9):
    user = [int(i) for i in input('Enter numbers: ').strip().split()]
    grid.append(user)


def possible(y, x, n):
    global grid
    for nums in range(0, 9):
        if grid[y][nums] == n:
            return False
    for j in range(0, 9):
        if grid[j][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for a in range(0, 3):
        for b in range(0, 3):
            if grid[y0 + a][x0 + b] == n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(f'\nAnswer: \n{np.matrix(grid)}')


solve()

