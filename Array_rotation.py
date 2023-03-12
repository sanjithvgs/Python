A=list(map(int,input("Enter the list element separated by space: ").split()))
B=int(input("Rotation time: "))
n=len(A)
B=B%n
# A=flip(A,0,n-1)
i=0
j=n-1
while i<j:
    A[i],A[j]=A[j],A[i]
    i+=1
    j-=1
# A=flip(A,0,k-1)
i=0
j=B-1
while i<j:
    A[i],A[j]=A[j],A[i]
    i+=1
    j-=1
# A=flip(A,k,n-1)
i=B
j=n-1
while i<j:
    A[i],A[j]=A[j],A[i]
    i+=1
    j-=1
print(f"List after roating {B} times:  ",A)

# output:
# Enter the list element separated by space: 1 2 3 4
# Rotation time: 2
# List after roating 2 times:   [3, 4, 1, 2]
