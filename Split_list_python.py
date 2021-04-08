''' Get a string from user and split into k values
    Print the split list without duplicate values
'''
import math
def merge_the_tools(string, k):
    lst=[]
    temp_lst=[]
    half=len(string)/k
    c=math.ceil(half)
    l=0
    i=0
    lst2=[]
    while i!=c:
        a=string[l:l+k]
        a=set (a)
        a=sorted(a)
        a=list (a)
        temp_lst.append(a)
        lst.append(temp_lst)
        l+=k
        i+=1
        temp_lst=[]
    print("The list after split the string into",k,"values without duplicate values are: ")
    for item in lst:
      print(item)

string, k = input("Enter a string: "), int(input("Enter the length to split: "))
merge_the_tools(string, k)