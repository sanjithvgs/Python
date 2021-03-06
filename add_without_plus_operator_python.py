# Addition of 2 numbers without using '+' operator

def fun(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a
x=int(input("Enter a number :"))
y=int(input("Enter another value :"))
print("The addition of two numbers is :",end="")
print(fun(x,y))