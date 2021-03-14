# Selection sorting..
    
lst=[]
len=int(input("Enter the length :"))
for i in range(len):
	a=input("Enter a element :")
	lst.append(a)
print(lst)

for i in range(len):
        min_index = i
        for j in range(i+1, len):
            
            if lst[j] < lst[min_index]:
                min_index = j
       
        lst[i], lst[min_index] = lst[min_index], lst[i]
print("The sorted list contain :")
print(lst)
