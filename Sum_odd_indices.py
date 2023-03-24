A = [1, 2, 3, 4, 5]
B = [   [0,2], 
        [1,4]   ]
prefix_odd=[]
temp=0
for i in range(len(A)):
    if i%2!=0:
        temp+=A[i]
        prefix_odd.append(temp)
    else:
        prefix_odd.append(temp)

result=[]
for ind in range(len(B)):
    left=B[ind][0]
    right=B[ind][1]
    if left==0:
        result.append(prefix_odd[right])
    else:
        result.append(prefix_odd[right]-prefix_odd[left-1])
print("The sum of odd indicies are: ",result)

# output:
# The sum of odd indicies are:  [2, 6]

# The subarray for the first query is [1, 2, 3] whose sum of odd indices is 2.
# The subarray for the second query is [2, 3, 4, 5] whose sum of odd indices is 6.