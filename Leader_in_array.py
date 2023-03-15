A=list(map(int,input("Enter list value: ").split()))
right_max=A[-1]
result=[]
result.append(A[-1])
for i in range(len(A)-1,-1,-1):
    if A[i]>right_max:
        result.append(A[i])
        right_max=A[i]
print("Leaders from right to left is:",result)

# output:
# 16 17 4 3 5 2
# Leaders from right to left is: [2, 5, 17]