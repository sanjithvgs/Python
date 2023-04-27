def solve(A, B):
    n=len(A)
    for i in range(2**n):
        total_sum=0
        for j in range(n):
            if (i>>j)&1:
                total_sum+=A[j]
        if total_sum==B:
            return 1
    return 0    

A = [1, 20, 13, 4, 5]
B = 18
print(solve(A,B))


# output:
# 1

# Sum of subsequence [1,13,4] is 18