''' Set operations
    --> Add -->pop -->Remove -->Discard
    remove() -> removes the element from the set only if the element is present in the set
    discard() -> removes element from the set, If the element is not present in the set, 
                      then an error or exception is raised
'''
n = int(input("Enter the length of set: "))
s = set(map(int, input("Enter the element separated by space: ").split()))
opr_len=int(input("Enter number of operations: "))
for i in range(opr_len):
    opr = list(map(str,input().split()))
    if opr[0]=="pop":
      try:
        s.pop()
      except:
        print("key Error")
    elif opr[0]=="remove":
      try:
        s.remove(int(opr[1]))
      except:
        print("key Error")
    elif opr[0]=="discard":
      s.discard(int(opr[1]))
    elif opr[0]=="add":
      s.add(int(opr[1]))
res=0
print("The set contain: ")
if len(s)==0:
  print("0")
else:
  print(s)