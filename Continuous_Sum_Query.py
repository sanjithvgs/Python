A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]   #B=[left,right,value]
beggar_value=[0]*A
for start,end,amount in B:
    beggar_value[start-1]+=amount
    if end<A:
        beggar_value[end]-=amount

for index in range(1,len(beggar_value)):
    beggar_value[index]+=beggar_value[index-1]

print(beggar_value)

# output:
# [10, 55, 45, 25, 25]

# Explaination:
# First devotee donated 10 coins to beggars ranging from 1 to 2. Final amount in each beggars pot after first devotee: [10, 10, 0, 0, 0]
# Second devotee donated 20 coins to beggars ranging from 2 to 3. Final amount in each beggars pot after second devotee: [10, 30, 20, 0, 0]
# Third devotee donated 25 coins to beggars ranging from 2 to 5. Final amount in each beggars pot after third devotee: [10, 55, 45, 25, 25]