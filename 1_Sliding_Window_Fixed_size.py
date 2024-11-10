# check if array contains a pair of duplicate values 
# where two duplicates are farther than two positions from k
# each other (i.e. arr[i] == arr[j] and abs(i - j ) + 1 <= k 
# O(n * k)

def bruteForceApproach(nums: list[int], k: int) -> bool:
    for left in range(len(nums)):
        for right in range(left + 1, min(len(nums), left + k)):
            if nums[left] == nums[right]:
                return True 
    return False 

print(bruteForceApproach([1, 2, 3, 2, 3, 3], 2))

# same problem using sliding window
# o(n)

def closeDuplicates(nums: list[int], k: int) -> bool:
    left = 0
    window = set()

    for right in range(len(nums)):
        if right - left + 1 > k:
            window.remove(nums[left])
            left += 1
        if nums[right] in window:
            return True 
        window.add(nums[right])
    return False 

print(closeDuplicates([1, 2, 3, 2, 3, 3], 2))
