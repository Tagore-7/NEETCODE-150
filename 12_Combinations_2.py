# Given n numbers (1 - n), return all possible combinations
# of size k. (n choose k math problem).

def combinations2(n, k):
    combs = []
    helper2(1, [], combs, n, k)
    return combs 


def helper2(i, curCombs, combs, n, k):
    if len(curCombs) == 2:
        combs.append(curCombs.copy())
        return 
    if i > n:
        return 

    for j in range(i, n + 1):
        curComb.append(j)
        helper2(j + 1, curComb, combs, n, k)
        curComb.pop() 

