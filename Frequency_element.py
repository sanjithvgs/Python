A = [1, 2, 1, 1]
B = [1, 2]
freq={}
for value in A:
    if value not in freq:
        freq[value]=1
    else:
        freq[value]+=1
result=[]
for query in B:
    if query not in freq:
        result.append(0)
    else:
        result.append(freq[query])
print(result)

# output:
# [3, 1]

# 1 occur 3 times
# 2 occur 1 times