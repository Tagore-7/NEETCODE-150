# low = 0, high = 100

#Binary search for range of values
def binarySearch(left, right):
    mid = (left + right) // 2

    while left <= right:
        if isCorrect(mid) > 0:
            right =  mid - 1
        elif isCorrect(mid) < 0:
            left = mid + 1
        else:
            return mid 
    
    return -1 

def isCorrect(n):
    if n > 10:
        return 1
    elif n < 10:
        retun -1
    else:
        return 0
