def removeDuplicate(str):
	s=set(str)
	s="".join(s)
	print("Without Order:",s)
	t=""
	for i in str:
		if(i in t):
			pass
		else:
			t=t+i
	print("With Order:",t)
	
str=str(input("Ente a string: "))
removeDuplicate(str)
