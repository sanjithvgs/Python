def fib(A):
    if A==0:
        return 0
    if A==1:
        return 1     
    return fib(A-1)+fib(A-2)

A=int(input("Enter a position to find digit in Fibonacci : "))
print(fib(A))

# output:
# Enter a position to find digit in Fibonacci : 9
# 34

# f(9) = f(8) + f(7) = 21 + 13  = 34