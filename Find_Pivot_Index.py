def pivotIndex(nums):
    prefix_sum=[]
    temp=0
    for val in nums:
        temp+=val
        prefix_sum.append(temp)
    lenn=len(nums)
    pivot_found=False
    for ind in range(lenn):
        if ind==0:
            left=0
            right=prefix_sum[lenn-1]-prefix_sum[ind]
        elif ind==lenn-1:
            left=prefix_sum[ind-1]
            right=0
        else:
            left=prefix_sum[ind-1]
            right=prefix_sum[lenn-1]-prefix_sum[ind]

        if left==right:
            return ind

    return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))

# output:

# 3

# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11