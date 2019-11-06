from util import Stack

# write a function that takes a 2d binary array and returns the
# number of 1 islands. An island consists of 1's that are connected
# to the north, south, east, or west

# for example:
# undirected graph
# unweighted
#Cyclic (undirected)

# Nodes are numbers, edges are connections between 1's

islands = [
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0],
]

# * islands[0] = [0, 1, 0, 1, 0] -- first row
# * islands[0][1] = 1 --- first row, second index

# Visit ech cell in the 2d array. When you come across a 1,
# Traverse it and mark all connected nodes as visited, then
# increment a counter


def get_islands_neighbors(x, y, matrix):
    neighbors = []
    # N y-1
    # S y+1
    # Check if a 1 to north
    if y > 0 and matrix[y-1][x] == 1:
        neighbors.append((x, y-1))
    # hceck south
    if y < len(matrix) - 1 and matrix[y+1][x] == 1:
        neighbors.append((x, y+1))
    if x < len(matrix[0]) - 1 and matrix[y][x+1] == 1:
        neighbors.append((x - 1, y))
    if x > 0 and matrix[y][x-1] == 1:
        neighbors.append((x+1, y))


def dft_islands(start_x, start_y, matrix, visited):
    """
    returns an updated visited matrix after a dft of matrix
    starting from x and y
    """
    # create empyt stack and push the starting vert ID
    s = Stack()
    s.push((start_x, start_y))
    # while not empty
    while s.size() > 0:
        v = s.pop()
        x = v[0]
        y = v[1]
        if not visited[y][x]:
            visited[y][x] = True
            for neighbor in get_islands_neighbors(x, y, matrix):
                s.push(neighbor)
    return visited


def island_counter(matrix):
    # Create a visited matrix w/ the same dimensions as the islands
    # matrix
    visited = []
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    for i in range(len(matrix)):
        visited.append([False] * matrix_width)
    # create a counter, start at 0
    counter = 0

    # For each cell in the 2d array...
    for x in range(matrix_width):
        for y in range(matrix_height):
            # When you come across a 1,
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    # DFT it and mark connected nodes as visited
                    visited = dft_islands(x, y, matrix, visited)
        # Traverse it and mark all connected nodes as visited, then
        # increment a counter
                    counter += 1
    return counter


island_counter(islands)  # returns 4
