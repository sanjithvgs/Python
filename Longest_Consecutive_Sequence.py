def longestConsecutive(A):
	hash_set=set()
	for val in A:
		hash_set.add(val)
	large_count=0
	current_count=0
	current_num=0
	for val in A:
		if val-1 not in hash_set:
			current_num=val
			current_count=1
		while current_num+1 in hash_set:
			current_num+=1
			current_count+=1
		large_count=max(current_count,large_count)
	return large_count

A = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(A))

# output:
# 4

# The set of consecutive elements will be [1, 2, 3, 4].