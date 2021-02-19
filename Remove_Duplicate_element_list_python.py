# Remove Duplicate element in the list
num = int(input("Enter the size of list: "))
lst=[]
for i in range(num):
  a=input()
  lst.append(a)
dup_items = set()
uniq_items = []
for x in lst:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)
   
