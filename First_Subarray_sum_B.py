def solve(A, B):
    result_list=[]
    start_index=0
    end_index=0
    current_sum=0
    flag=False
    while start_index<len(A) and end_index<len(A):
        if start_index>end_index:
            end_index=start_index
            current_sum+=A[end_index]
        if current_sum<B:
            current_sum+=A[end_index]
            end_index+=1
        if current_sum>B:
            current_sum-=A[start_index]
            start_index+=1
        if current_sum==B:
            flag=True
            break
    if flag:
        for ind in range(start_index,end_index):
            result_list.append(A[ind])
        return result_list
    else:
        temp_result=[-1]
        return temp_result

A = [1, 2, 3, 4, 5]
B = 5
print("First subarray with sum",B,"is: ",end="")
print(solve(A,B))

# output:
# First subarray with sum 5 is: [2, 3]