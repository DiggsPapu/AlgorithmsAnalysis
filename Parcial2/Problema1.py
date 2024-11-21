def count_combinations(start_digit, remaining_length, moves, memo):
    # Base case
    if remaining_length == 1:
        return 1
    # Check memoization
    if (start_digit, remaining_length) in memo:
        return memo[(start_digit, remaining_length)]
    # Counting combinations
    total_combinations = 0
    # Move through any posible move
    for next_digit in moves[start_digit]:
        # recursive call of the smaller lengths
        total_combinations += count_combinations(next_digit, remaining_length - 1, moves, memo)
    # Store in memoization
    memo[(start_digit, remaining_length)] = total_combinations
    # return combinations
    return total_combinations

def total_combinations(n):
    # Permited moves per digit
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
    
    # Memoization dictionary
    memo = {}
    # Init total combinations
    total = 0
    # Count from 0 to 9
    for digit in list(moves.keys()):
        # Append total count combinations per digit
        total += count_combinations(digit, n, moves, memo)
    return total
n = 10
print(total_combinations(n))
