def solve(A):
    hash_map={}
    min_val=100000
    for ind in range(len(A)):
        if A[ind] in hash_map:
            min_val=min(min_val,ind-hash_map[A[ind]])
        else:
            hash_map[A[ind]]=ind
    if min_val!=100000:
        return min_val
    return -1

A = [7, 1, 3, 4, 1, 7]
print(solve(A))

# output:
# 3

# Here we have 2 options:
# 1. A[1] and A[4] are both 1 so (1,4) is a special pair and |1-4|=3.
# 2. A[0] and A[5] are both 7 so (0,5) is a special pair and |0-5|=5.
# Therefore the minimum possible distance is 3. 