
# Recursive implementation of n! (n-factorial) calculation
def factorial(n):
    if n<= 1:
        return 1
    return n * factorial(n -1)

