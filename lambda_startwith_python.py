'''Check whether the given string is start with given letter or not '''

starts_with = lambda x: True if x.startswith(p) else False
st=str(input("Enter the string: "))
p=str(input("Enter the starting word: "))
a=starts_with(st)
if a:
	print("The string is start with given letter ")
else:
	print("The string is not start with given letter ")
