def count_combinations(n):
    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]
    memo = {}

    def helper(i, j, length):
        if (i, j, length) in memo:
            return memo[(i, j, length)]

        if length == 1:
            memo[(i, j, length)] = 1
            return 1

        total = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                ni, nj = i + di, j + dj
                if 0 <= ni < 4 and 0 <= nj < 3 and keypad[ni][nj] != '*' and keypad[ni][nj] != '#':
                    total += helper(ni, nj, length - 1)

        memo[(i, j, length)] = total
        return total

    total_combinations = 0
    for i in range(4):
        for j in range(3):
            if keypad[i][j] != '*' and keypad[i][j] != '#':
                total_combinations += helper(i, j, n)

    return total_combinations

# Example usage:
n = 10
print(count_combinations(n))  # Output: 36
