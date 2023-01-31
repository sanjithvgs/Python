def largest(A):
    temp=[]
    for row in range(len(A)):
        maxi=0
        for col in range(len(A[0])):
            if A[row][col]>maxi:
                maxi=A[row][col]
        temp.append(maxi)
    return temp

row,col=map(int,input("Enter row and column of 2D list: ").split())
A=[]
for i in range(row):
    row=[]
    for j in range(col):
        row.append(int(input(f"Enter element for row {i} and column {j}: ")))
    A.append(row)
print("largest element in each rows are:",largest(A))

#A=[[1,10],[2,8]]
#o/p: [10,8]
