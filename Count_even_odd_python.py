def fun(num):
	eve=0
	odd=0
	for i in range(num):
		if(lst[i]%2==0):
			eve+=1
		else:
			odd+=1
	print("The count of even number is :" ,eve)
	print("The count of odd number is :" ,odd)

lst=[]
num=int(input("Enter the length of list: "))
for i in range(num):
	a=int(input())
	lst.append(a)
fun(num)