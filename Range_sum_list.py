A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]
sum=0
prefix=[]
for val in A:
    sum+=val
    prefix.append(sum)
result=[]
for left,right in B:
    if left==0:
        result.append(prefix[right])
    else:
        result.append(prefix[right]-prefix[left-1])
print("The sum for given range is:",result)

# output:
# The sum for given range is: [10, 5]