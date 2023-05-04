def solve(A):
    prefix_sum=[]
    temp=0
    for val in A:
        temp+=val
        if temp==0:
            return 1
        prefix_sum.append(temp)
    repeat_dict={}
    for val in prefix_sum:
        if val in repeat_dict:
            repeat_dict[val]+=1
            return 1
        else:
            repeat_dict[val]=1
    return 0

A = [-1, 1,2,5,7,10]
print(solve(A))

# output:
# 1

# sub_array [-1,1] sum is 0