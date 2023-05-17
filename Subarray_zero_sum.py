A = [1, -1, -2, 2]
prefix_sum=[]
temp=0
for val in A:
    temp+=val
    prefix_sum.append(temp)
zero_sum_count=0
for val in prefix_sum:
    if val==0:
        zero_sum_count+=1
repeat_dict={}
for val in prefix_sum:
    if val not in repeat_dict:
        repeat_dict[val]=1
    else:
        repeat_dict[val]+=1
for val in repeat_dict:
    if repeat_dict[val]>1:
        zero_sum_count+=(repeat_dict[val]-1)*(repeat_dict[val])//2

print("Subarry count wiht zero sum is: ",zero_sum_count)

# output:
# Subarry count wiht zero sum is:  3


# The subarrays with zero sum are [1, -1], [-2, 2] and [1, -1, -2, 2].