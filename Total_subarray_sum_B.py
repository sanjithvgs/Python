def solve(A, B):
    hash_map={}
    prefix_sum=[]
    temp=0
    result_count=0
    for val in A:
        temp+=val
        prefix_sum.append(temp)
    for ind in range(len(A)):
        x=prefix_sum[ind]-B
        if prefix_sum[ind]==B:
            result_count+=1
        if x in hash_map:
            result_count+=hash_map[x]
        if prefix_sum[ind] not in hash_map:
            hash_map[prefix_sum[ind]]=1
        elif prefix_sum[ind] in hash_map:
            hash_map[prefix_sum[ind]]+=1
    return result_count

A = [1, 0, 1]
B = 1
print(solve(A,B))


# output:
# 4

# [1], [1, 0], [0, 1] and [1] are four subarrays having sum 1.