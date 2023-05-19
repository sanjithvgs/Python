def solve(A, B):
    freq_set=set()
    count=0
    for ind in range(len(B)):
        if A-B[ind] in freq_set:
            return 1
        if B[ind] not in freq_set:
            freq_set.add(B[ind])
    return 0

A = 8   
B = [3, 5, 1, 2, 1, 2]
print(solve(A,B))

# output:
# 1

# It is possible to obtain sum 8 using 3 and 5.