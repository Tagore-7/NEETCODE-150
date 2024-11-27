# check if an array is a palindrome 

def checkArrPalinDrome(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True 

print(checkArrPalinDrome([1, 2, 7, 7, 2, 1]))

# Given the sorted array of integers return the indices of two elements that add upto the given target 
# there is one exactly one solution 

def targetSum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] > target:
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            return [left, right]

print(targetSum([-1, 2,3, 4, 8, 9],7))

