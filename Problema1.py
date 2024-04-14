# Define el teclado móvil del Nokia 3230
keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]
keys = {
    '1':['1','2','4'],
    '2':['1','2','3', '5'],
    '3':['2','3', '6'],
    '4':['1','4','5','7'],
    '5':['2','4','5','6','8'],
    '6':['3','5','6','9'],
    '7':['4','7','8'],
    '8':['5','7','8','9','0'],
    '9':['6','8','9'],
    '0':['8','0']
    }
# DIVIDE AND CONQUER IMPLEMENTATION
def countCombinationsDivideAndConquer(n):
    def recursivePart(key, newCombination, n):
        # Si llego al caso base
        if len(newCombination)==n:
            return (newCombination)
        newCombinations = []
        # Se le va agregando 1 digito
        for digit in keys.get(key):
            value = recursivePart(key, newCombination+digit, n)
            if type(value)==str:
                newCombinations.append(value)
            else: 
                newCombinations.extend(value)
        return newCombinations
    totalCombinations = []
    for i in range(0, len(keypad)):
        for j in range(0, len(keypad[i])):
            key = keypad[i][j]
            if key!='*' and key!='#':
                totalCombinations.extend(recursivePart(key, key,n))
    # print(totalCombinations)
    print(len(totalCombinations))

def count_combinations(keypad, moves, start_digit, remaining_length, memo):
    # Base case: si la longitud restante es 0, devuelve 1
    if remaining_length == 0:
        return 1
    
    # Checar memoización para evitar cálculos repetidos
    if (start_digit, remaining_length) in memo:
        return memo[(start_digit, remaining_length)]
    
    # Iniciar el conteo de combinaciones desde el dígito inicial
    total_combinations = 0
    
    # Recorrer cada movimiento posible desde el dígito inicial
    for next_digit in moves[start_digit]:
        # Llamar recursivamente para la longitud restante menor
        total_combinations += count_combinations(keypad, moves, next_digit, remaining_length - 1, memo)
    
    # Almacenar el resultado en memoización
    memo[(start_digit, remaining_length)] = total_combinations
    
    # Devolver el total de combinaciones calculadas
    return total_combinations

def total_combinations(n):
    # Definir la estructura del teclado y los movimientos permitidos desde cada dígito
    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]

    # Mapear los movimientos permitidos desde cada dígito
    moves = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }
    
    # Crear un diccionario de memoización para almacenar resultados
    memo = {}
    
    # Inicializar el total de combinaciones
    total = 0
    
    # Contar combinaciones para cada dígito inicial del 0 al 9
    for digit in '0123456789':
        total += count_combinations(keypad, moves, digit, n, memo)
    
    return total

# Calcular el total de combinaciones posibles para n = 10
n = 4
result = total_combinations(n-1)
print(result)
countCombinationsDivideAndConquer(n)
# print(count_combinations(n))  # Output: Combinaciones posibles para n = 3
