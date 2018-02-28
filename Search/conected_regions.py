def get_neighbors(current, grid):
    n = len(grid)
    m = len(grid[0])

    i, j = current
    neighbors = []
    indcies = [(i - 1, j    ),
               (i - 1, j + 1),
               (i    , j + 1),
               (i + 1, j + 1),
               (i + 1, j    ),
               (i + 1, j - 1),
               (i    , j - 1),
               (i - 1, j - 1)]

    for i, j in indcies:
        if 0 <= i < n and  0 <= j < m and grid[i][j]:
            neighbors.append((i, j))

    return neighbors


def get_region(i, j, grid):
    """returns connected cells to (i, j) in grid"""
    visited = []
    frontier = [(i, j)]

    while frontier:
        current = frontier.pop(0)

        if current in visited:
            continue

        neighbors = get_neighbors(current, grid)
        frontier += neighbors
        visited.append(current)

    return visited


def getBiggestRegion(grid):
    biggest_region_size = 0
    visited = []

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if (i, j) not in visited and grid[i][j]:
                region = get_region(i, j, grid)
                biggest_region_size = max(len(region), biggest_region_size)
                visited += region

    return biggest_region_size

a = [[1, 1, 0, 0],
     [0, 1, 1, 1],
     [0, 0, 1, 0],
     [1, 0, 0, 0]]

b = [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]

print(getBiggestRegion(a))
# print(get_neighbors((0, 1), b))
print(getBiggestRegion(b))

# n = int(input().strip())
# m = int(input().strip())
# grid = []
# for grid_i in range(n):
#     grid_t = list(map(int, input().strip().split(' ')))
#     grid.append(grid_t)
# print(getBiggestRegion(grid))
