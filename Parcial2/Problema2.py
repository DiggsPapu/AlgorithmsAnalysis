def printMatrix(matrix):
    for line in matrix:
        print(line)
def find_largest_cross_size(grid):
    # length matrix
    n = len(grid)
    # Create auxiliar matrixes
    left = [[0] * n for x in range(n)]
    right = [[0] * n for x in range(n)]
    top = [[0] * n for x in range(n)]
    bottom = [[0] * n for x in range(n)]
    # fill matrixes
    # moves from left to right and from top to bottom
    for i in range(n):
        for j in range(n):
            # left
            if (grid[i][j] == 1):
                if j == 0:
                    left[i][j] = 1
                else:
                    left[i][j] = left[i][j - 1] + 1               
 
            # top
            if (grid[j][i] == 1):
                if j == 0:
                    top[j][i] = 1
                else:
                    top[j][i] = top[j - 1][i] + 1
 
            # make move right to left and bottom to top
            j = n - 1 - j
 
            # bottom
            if (grid[j][i] == 1):
                if j == n-1:
                    bottom[j][i] = 1
                else:
                    bottom[j][i] = bottom[j + 1][i] + 1
                    
            # right
            if (grid[i][j] == 1):
                if j == n-1:
                    right[i][j] = 1
                else:
                    right[i][j] = right[i][j + 1] + 1
            # revert to top to bottom and left to right
            j = n - 1 - j
            
    printMatrix(right)
    print("\n")
    printMatrix(left)
    print("\n")
    printMatrix(top)
    print("\n")
    printMatrix(bottom)
    print("\n")
    max_cross_size = 0
    for i in range(n):
        for j in range(n):
            # If grid[i][j] is 1, calculate the cross size
            if grid[i][j] == 1:
                # Get the smallest cross size
                cross_size = min(left[i][j]-1, right[i][j]-1, top[i][j]-1, bottom[i][j]-1)
                if (cross_size>0):
                    # Update max cross size, which is max
                    max_cross_size = max(max_cross_size, cross_size*4+1)
    return max_cross_size

# Pruebas
grid1 = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
]

grid2 = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0]
]

print(find_largest_cross_size(grid1))  # Salida esperada: 17
print(find_largest_cross_size(grid2))  # Salida esperada: 0
