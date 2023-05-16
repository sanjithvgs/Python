def getSum(B, C):

    tree_dict={}
    flag=False
    for val in C:
        if val in tree_dict:
            tree_dict[val]+=1
        else:
            tree_dict[val]=1

    height_result=0
    for val in tree_dict:
        if tree_dict[val]==B:
            height_result+=val
            flag=True

    if not flag:
        return -1
    return height_result

B=2 
C=[1,2,2,3,3]
print(getSum(B,C))

# output:
# 5


# There are 3 distinct numbers in the array which are 1,2,3.
# Out of these, only 2 and 3 occur twice. Therefore the answer is sum of 2 and 3 which is 5.