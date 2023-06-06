def palin(A,start,end):
    if start>end:
        return 1
    if A[start]==A[end] and palin(A,start+1,end-1):
        return 1
    return 0

A=input("Enter a string to check palindrome: ")
print(palin(A,0,len(A)-1))

# output:

# Enter a string to check palindrome: madam
# 1