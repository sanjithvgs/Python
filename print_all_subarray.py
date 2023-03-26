A=list(map(int,input("Enter list value: ").split()))
n=len(A)
result=[]
for start in range(n):
    for end in range(start,n):
        temp=[]
        for ind in range(start,end+1):
            temp.append(A[ind])
        result.append(temp)
print("All subarray in give list: ", result)

# output:
# Enter list value: 1 2 3
# All subarray in give list:  [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]