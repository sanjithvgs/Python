A = [1, -2, 1, 2]
prefix_sum=[]
temp=0
for val in A:
    temp+=val
    prefix_sum.append(temp)
max_len=0
dict_first={}
for ind in range(len(prefix_sum)):
    if prefix_sum[ind]==0:
        max_len=max(max_len,ind+1)
    else:
        if prefix_sum[ind] in dict_first:
            curr_ind=ind
            first_ind=dict_first[prefix_sum[ind]]
            curr_len=curr_ind-first_ind
            max_len=max(max_len,curr_len)
        else:
            dict_first[prefix_sum[ind]]=ind
print("The longest subarray with sum 0 is :", max_len)           


# output:
# The longest subarray with sum 0 is : 3
# [1, -2, 1] is the largest subarray which sums up to 0.