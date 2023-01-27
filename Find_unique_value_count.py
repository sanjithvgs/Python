tup=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
lst=[]
for value in tup:
    if value not in lst:
        print(value,":",tup.count(value))
        lst.append(value)

#   o/p: 
#   10 : 3
#   8 : 4
#   5 : 2
#   2 : 2
#   15 : 1 