# Find the length of the longest subarray, with the same value in each position 
def longestSubArray(nums: list[int]):
    length = 0
    left = 0

    for right in range(len(nums)):
        if nums[right] != nums[left]:
            left = right 

        length = max(length, right - left + 1)

    return length 

print(longestSubArray([4,2,2, 3, 3, 3]))


# Find the minimum length subarray, where the sum is greater than or equal to the target. Assume all values are positive 
def shortedSubArray(nums: list[int], target: int):
    left, total_sum = 0, 0
    length = float("inf")

    for right in range(len(nums)):
        total_sum += nums[right]

        while total_sum >= target:
            length = min(length, right - left + 1)
            total_sum -= nums[left]    
            left += 1
    return length if length != float("inf") else 0

print(shortedSubArray([2,3,1,2,4,3], 6))
