def num(A):
    if A<1:
        return            
    print(A,end=" ")
    return num(A-1)

A=10
num(A)

# output:
# 10 9 8 7 6 5 4 3 2 1 