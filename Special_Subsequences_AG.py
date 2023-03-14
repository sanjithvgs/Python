A=input("Enter a string: ")
result=0
g_count=0
for i in range(len(A)-1,-1,-1):
    if A[i]=='G':
        g_count+=1
    elif A[i]=='A':
        result+=g_count
print("Count for pair A to G is:",result)

# output:
# Enter a string:  ABCGAG
# Count for pair A to G is: 3