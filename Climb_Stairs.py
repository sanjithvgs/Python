def climbStairs(n):
    if n==1:
        return 1
    if n==2:
        return 2
    lst=[0]*(n+1)
    lst[1]=1
    lst[2]=2
    for idx in range(3,n+1):
        lst[idx]=lst[idx-1]+lst[idx-2]
        
    return lst[n]

n=3
print(climbStairs(n))


# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step