A = 5
B = 2
if ((A>>B)&1):
    A=A^(1<<B)
print(A)

# output:
# 1


# N = 5 which is 101 in binary. We unset the 2-nd bit