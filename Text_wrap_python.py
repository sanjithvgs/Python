import math,re
def wrap(string, max_width):
    j=max_width
    i=0
    c=0
    string = re.sub('\s+', '', string)
    a=(len(string))/max_width
    b=math.ceil(a)
    while c<=b-1:
      print(string[i:j])
      i=i+max_width
      j=j+max_width
      c+=1

string=str(input("Enter the string: "))
max_width=int(input("Enter the width of string in each line: "))
wrap(string, max_width)