A=int(input("Enter a value: "))
B=int(input("Enter bit value to unset from right: "))
for i in range(B):
    if (A>>i)&1:
        A=A^(1<<i)

print(A)

# output:
# Enter a value: 93
# Enter bit value to unset from right: 4
# 80

# A = 93, B = 4
# A in binary = 1011101
# A should become = 1010000 = 80.