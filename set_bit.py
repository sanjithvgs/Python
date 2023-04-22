# question:
# Set the A-th bit and B-th bit in 0, and return output in decimal

A = 3
B = 5
N=0
N=N^(1<<A)
if A!=B:
    N=N^(1<<B)
print(N)

# output:
# 40

# The binary expression is 101000 which is 40 in decimal.