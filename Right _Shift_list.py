n=int(input("Enter the count of list"))  #5
temp=[]
lst=[]
temp=input("Enter list element with space").split()  # 1 2 3 4 5
for item in temp:
    lst.append(int(item))
s=lst[-1]
lst.insert(0,s)
lst.pop()
print("List element after right shif: ")
for ele in lst:
    print(ele,end=" ")   # 5 1 2 3 4
