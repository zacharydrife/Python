def solution(matrix):
    n = len(matrix)
    min_changes = float('inf')

    for y in [0, 1, 2]:
        for background in [0, 1, 2]:
            if y == background:
                continue

            changes = 0

            for i in range(n):
                for j in range(n):
                    if ((i == j or i + j == n - 1 or (j == n // 2 and i >= n // 2)) and matrix[i][j] != 2) or \
                       ((i != j and i + j != n - 1 and (j != n // 2 or i < n // 2)) and matrix[i][j] != background):
                        changes += 1

            min_changes = min(min_changes, changes)

    return min_changes

# Example usage:
matrix1 = [
    [1, 0, 2],
    [1, 2, 0],
    [0, 2, 0]
]
result1 = solution(matrix1)
print(result1)  # Output should be 2

matrix2 = [
    [2, 0, 0, 0, 2],
    [1, 2, 1, 2, 0],
    [0, 1, 2, 1, 0],
    [0, 0, 2, 1, 1],
    [1, 1, 2, 1, 1]
]
result2 = solution(matrix2)
print(result2)  # Output should be 8
