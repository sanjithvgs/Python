A=11
count=0
while A>0:
    if A&1:
        count+=1
    A=A>>1

print(count) 

# output:
# 3

# 11 is represented as 1011 in binary.