def solve(A):
   hash_set=set()
   for ind in range(len(A)):
       string=str(A[ind][0])+"@"+str(A[ind][1])
       hash_set.add(string)

   return len(hash_set)

A = [[1, 1], [2, 2], [2, 2], [1, 1], [1, 1]]
print(solve(A))

# output:
# 2


# There are 2 unique points in the given array. They are [1, 1] and [2, 2].
