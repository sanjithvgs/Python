A = [3, 3, 3, 9, 0, 1, 0]
freq_one={}
for val in A:
    if val not in freq_one:
        freq_one[val]=1
    else:
        freq_one[val]+=1
resul_count=0
for val in freq_one:
    if freq_one[val]==1:
        resul_count+=1
print("The count of elements with frequncy 1 is: ",resul_count)

# output:
# The count of elements with frequncy 1 is:  2