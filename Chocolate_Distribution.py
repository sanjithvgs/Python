A=[3, 4, 1, 9, 56, 7, 9, 12]
B=5

A.sort()
init=0
mini_sum=float('inf')
while B<=len(A):
    temp_sum=A[B-1]-A[init]
    B+=1
    init+=1
    mini_sum=min(temp_sum,mini_sum)

print(mini_sum)

# output:
# 6