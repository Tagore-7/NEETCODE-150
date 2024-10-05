arr = [1, 3, 3, 4, 5, 6, 7, 8]

def binarySearch(arr, target):
    left = 0
    right = 0
    arr.sort()
    while(left <= right):
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return arr[mid]
    return -1
            
