def swap_case(s):
    lst=[]
    for i in range(len(s)):
        if s[i].isupper():
          a=s[i].lower()
          lst.append(a)
        elif s[i].islower():
          b=s[i].upper()
          lst.append(b)
        else:
          lst.append(s[i])
    for item in lst:
      print(item,end="")

s = input("Enter a string: ")
swap_case(s)