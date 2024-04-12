def find_largest_cross_size(grid):
    # Obtener el tamaño de la matriz cuadrada
    n = len(grid)

    # Crear matrices auxiliares
    left = [[0] * n for _ in range(n)]
    right = [[0] * n for _ in range(n)]
    top = [[0] * n for _ in range(n)]
    bottom = [[0] * n for _ in range(n)]

    # Llenar la matriz left
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                if j == 0:
                    left[i][j] = 1
                else:
                    left[i][j] = left[i][j - 1] + 1

    # Llenar la matriz right
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if grid[i][j] == 1:
                if j == n - 1:
                    right[i][j] = 1
                else:
                    right[i][j] = right[i][j + 1] + 1

    # Llenar la matriz top
    for j in range(n):
        for i in range(n):
            if grid[i][j] == 1:
                if i == 0:
                    top[i][j] = 1
                else:
                    top[i][j] = top[i - 1][j] + 1

    # Llenar la matriz bottom
    for j in range(n):
        for i in range(n - 1, -1, -1):
            if grid[i][j] == 1:
                if i == n - 1:
                    bottom[i][j] = 1
                else:
                    bottom[i][j] = bottom[i + 1][j] + 1
    # Encontrar el tamaño de la cruz más grande
    max_cross_size = 0
    
    
    # Recorremos la matriz grid
    for i in range(n):
        for j in range(n):
            # Si grid[i][j] es 1, calculamos el tamaño de la cruz
            if grid[i][j] == 1:
                # Obtenemos el tamaño de la cruz mínima
                cross_size = min(left[i][j]-1, right[i][j]-1, top[i][j]-1, bottom[i][j]-1)
                if (cross_size>0):
                    # Actualizamos el tamaño máximo
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
