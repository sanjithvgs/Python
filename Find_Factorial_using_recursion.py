def fact(A):
    if A<=1:
        return 1
    return fact(A-1)*A

A=int(input("Enter a number to find factorial: "))
print(fact(A))

# output:
# Enter a number to find factorial: 4
# 24