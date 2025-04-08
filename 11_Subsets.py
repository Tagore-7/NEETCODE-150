#without duplicates 
def subSetsWithoutDuplicates(nums):
    subsets, curSet = [], []
    helper(0, nums, subsets, curSet)
    return subsets

def helper(i, nums, subsets, curSet):
    if i >= len(nums):
        subsets.append(curSet.copy())
        return 

    curSet.append(nums[i))
    helper(i + 1, nums, subsets, curSet)
    curSet.pop()

    helper(i + 1, nums, subsets, curSet)



# with duplicates 
def subSetswithDuplicates(nums):
    subsets, curSet = [], []
    helper2(0, nums, subsets, curSet) 
    return subsets

def helper2(i, nums, subsets, curSet):
    if i >= len(nums):
        subsets.append(curSet.copy())
        return 

    curSet.append(nums[i])
    helper2(i + 1, nums, subsets, curSet)
    curSet.pop()

    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1


    helper2(i, nums, subsets, curSet) 



