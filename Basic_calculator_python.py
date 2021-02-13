opt=int(input("Enter any one option 1.Add 2.Sub 3.Mul 4.Div \n"))
if opt in (1,2,3,4):
	 a=int(input("Enter a number : "))
	 b=int(input("Enter another number : "))

	 if (opt == 1):
	 	result = a + b
	 	print("Addition value : " , result )
	 	

	 elif (opt == 2):
	 	result= a - b
	 	print("subtraction value : " , result )

	 
	 elif (opt == 3):
	 	result= a * b
	 	print("Multiple value : " , result )

	 
	 elif (opt == 4):
	 	result= a / b 
	 	print("Division value : " , result )

else:
		print ("invalid number") 	 	 