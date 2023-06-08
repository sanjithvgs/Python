def digit(A):
    if A==0:
        return 0
    return digit(A//10)+A%10

A=int(input("Enter a digit to find it's sum: "))
print(digit(A))

# output:
# Enter a digit to find it's sum: 64
# 10

# 6+4=10