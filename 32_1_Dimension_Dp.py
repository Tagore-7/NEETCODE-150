# brute force 
def bruteforce(n):
    if n <= 1:
        return n
    return bruteforce(n - 1) + bruteforce(n - 2)

print(bruteforce(5))

# Memoization top down apporach dynamic programming
def memoization(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)
    return cache[n]
print(memoization(5, {}))

# dynamic programming bottom-up arroach
def dp(n):
    if n < 2:
        return n
    dp = [0, 1]
    i = 2

    while i <= n:
        temp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = temp
        i += 1

    return dp[1]

print(dp(7))


