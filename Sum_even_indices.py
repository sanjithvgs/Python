A = [2, 1, 8, 3, 9]
B = [   [0,3], 
        [2,4]   ]
temp=0
prefix_even=[]
for i in range(len(A)):
    if i%2==0:
        temp+=A[i]
        prefix_even.append(temp)
    else:
        prefix_even.append(temp)

result=[]
for ind in range(len(B)):
    left=B[ind][0]
    right=B[ind][1]
    if left==0:
        result.append(prefix_even[right])
    else:
        result.append(prefix_even[right]-prefix_even[left-1])
print("The sum of even indicies are: ",result)

# output:
# The sum of even indicies are:  [10, 17]

# The subarray for the first query is [2, 1, 8, 3] whose sum of even indices is 10.
# The subarray for the second query is [8, 3, 9] whose sum of even indices is 17.