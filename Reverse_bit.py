A=int(input("Enter a value to reverse bits: "))
result=0
for i in range(32):
    bit=(A>>i)&1
    result=result|(bit<<(31-i))
print(result)

# output:
# Enter a value to reverse bits: 3
# 3221225472


# Before reverse:     00000000000000000000000000000011    
# After reverse:      11000000000000000000000000000000
