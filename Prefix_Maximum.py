A=list(map(int,input("Enter list value: ").split()))
for index in range(1,len(A)):
    if A[index]<A[index-1]:
        A[index]=A[index-1]
    else:
        A[index]=A[index]
print("Prefix Maximum values are: ",A)

# output:
# Enter list value: 16 8 24 9 25 17
# Prefix Maximum values are:  [16, 16, 24, 24, 25, 25]