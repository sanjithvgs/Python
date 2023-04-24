A=int(input("Enter a value: "))
B=int(input("Enter bit value: "))
A=(1<<B)^A
print(A)

# output:
# Enter a value: 5
# Enter bit value: 2
# 1


# Given N = 5 which is 101 in binary. 
# The 2-nd bit is set
# so we make it unset as 001 in binary