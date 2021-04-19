# Count Alphabets and Digits from user Inputs

a=input("Enter a Input :")
lst=[]
lst=a
str_cnt=0
int_cnt=0
othr_cnt=0

for i in range(len(lst)):
  z=lst[i]
  if z.isdigit() :
    int_cnt+=1
  elif z.isalpha():
    str_cnt+=1
  else:
    othr_cnt+=1

print("The count of Strings are :",str_cnt)
print("The count of Digits are :",int_cnt)
print("Other's count :",othr_cnt)
