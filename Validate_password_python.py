import re
p= input("Input your password for validate: ")
x = True
while x:
	if (len(p)<6 or len(p)>12):
		print("password should less than 6 and larger than 12\n")
		break
	elif not re.search("[a-z]",p):
		print("password should contain alphabet from a-z\n")
		break
	elif not re.search("[0-9]",p):
		print("password should contain atleast one number\n")
		break
	elif not re.search("[A-Z]",p):
		print("password should contain alphabet from A-Z\n")
		break
	elif not re.search("[$#@]",p):
		print("password should contain any special character\n")
		break
	elif re.search("\s",p):
		print("password should not contain any blank space\n")
		break
	else:
		print("Valid Password..")
		x=False
		break

if x:
    print("Not a Valid Password..!")