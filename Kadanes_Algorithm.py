# find a non-empty subarray with the largest sum 
# brute force: O(n^2)

def bruteForce(nums):
    maxSum = nums[0]

    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    
    return maxSum

print(bruteForce([4, -1, 2, -7, 3, 4]))


# kadanes algorithm O(n)
def kd(nums):
    maxSum = nums[0]
    curSum = 0

    for num in nums:
        curSum += num 
        curSum = max(curSum, 0)

        maxSum = max(maxSum, curSum)
    
    return maxSum

print(kd([4, -1, 2, -7, 3, 4]))

# sliding window varaiation with kd 
# return indices contributing to the maxSum 
def sw(nums):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum  = 0
            L = R 

        curSum += nums[R]
        if curSum > maxSum:
            maxSum =  curSum
            maxL, maxR = L, R 

    return [maxL, maxR]

print(sw([4, -1, 2, -7, 3, 4]))

