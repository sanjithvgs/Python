n=int(input("Enter the number of elements: "))
A=list(map(int, input().split()))
maxi=0
for item in A:
    if item>maxi:
        maxi=item
ans=0
for i in A:   #To check if list contain any mutiple value
    if i>ans and i<maxi:
        ans=i
print("The second largest element in list is:")
if ans==0:
    print(-1)
else:
    print(ans)
