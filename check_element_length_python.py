''' To check whether given element is present 
       before the given length 
'''

def list_front(nums,c,z,y):
  count=False
  if c<=z:
    for i in range(c):
      if nums[i]==y:
        count=True
  else:
    for i in range(z):
      if nums[i]==y:
        count=True
  if count is True:
    print ("The element",y,"is Present until",z,"elements in the list")
  else:
    print ("The element",y,"is Not Present until",z,"elements in the list")

lst=[]
cnt=int(input ("Enter the length: "))
for i in range(cnt):
  a=int(input("Enter the element: "))
  lst.append(a)
y=int(input("Enter a element to check in list: "))
z=int(input("Enter the length until to check specify element: "))
print(lst)
list_front(lst,cnt,z,y)   