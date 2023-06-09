def solve(A):
    def digit(A):
        if A==0:
            return A
        result=digit(A//10)+A%10
        if result>9:
            result=digit(result)
            return result
        else:
            return result
    if digit(A)==1:
        return 1
    return 0


A=int(input("Enter a number: ")) 
print(solve(A))


# output:
# Enter a number: 83557
# 1



#  Sum of digits of (83557) = 28
#  Sum of digits of (28) = 10
#  Sum of digits of (10) = 1. 
#  Single digit is 1, so it's a magic number. Return 1.

# Single digit is not 1 means it is not magic number