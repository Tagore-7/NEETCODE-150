# Brute Force - Time: O(2 ^ (n + m)), Space: O(n + m)

def bruteForce(r, c, rows, cols):
    if r >= rows or c >= cols:
        return 0

    if r == rows - 1 and c == cols - 1:
        return 1

    return bruteForce(r + 1, c, rows, cols) + bruteForce(r, c + 1, rows, cols)

print(bruteForce(0,0, 4, 4))


# Memoization - Time and Space: O(n * m) Top - down dynamic programming 

def memoization(r, c, rows, cols, cache):
    if r >= rows or c >= cols:
        return 0

    if cache[r][c]:
        return cache[r][c]

    if r == rows - 1 and c == cols - 1:
        return 1

    cache[r][c] = memoization(r + 1, c, rows, cols, cache) +  memoization(r, c + 1, rows, cols, cache)

    return cache[r][c]

print(memoization(0, 0, 4, 4, [[0] * 4 for _ in range(4)]))


# bottom - up appraoch dp 

def dp(rows, cols):
    prevRow = [0] * cols 

    for r in range(rows - 1, -1, -1):
        currRow = [0] * cols 
        currRow[cols - 1] = 1
        for c in range(cols - 2, -1, -1):
            currRow[c] = currRow[c + 1] + prevRow[c]
        prevRow = currRow 
    
    return prevRow[0]

print(dp(4, 4))
