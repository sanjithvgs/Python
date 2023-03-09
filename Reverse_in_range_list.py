A=list(map(int,input("Enter the list element separated by space: ").split()))
B=int(input("Enter the start range: "))
C=int(input("Enter the end range: "))
i=B
j=C
while i<j:
    A[i],A[j]=A[j],A[i]
    i+=1
    j-=1
print(A)

# output:
# Enter the list element separated by space: 1 2 3 4
# Enter the start range: 2
# Enter the end range: 3
# [1, 2, 4, 3]