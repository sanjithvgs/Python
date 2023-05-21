def solve(A, B):
    hash_set=set()
    for val in A:
        hash_set.add(val)
    for ind in range(len(A)):
        if B+A[ind] in hash_set and B!=0:
            return 1            
    return 0  

A = [5, 10, 3, 2, 50, 80]
B = 78 
print("Pair with given difference is: ",end="")
print(solve(A,B))

# output:
# Pair with given difference is: 1


#  Pair (80, 2) gives a difference of 78.