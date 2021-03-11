# Operations in Stack (using List)

stack=[]
opt=0
top=int(input("Enter the size of stack: "))
while (opt!=4):
  
  opt=int(input("Enter option: 1.Push 2.Pop 3.Display_stack 4.Exit : \n"))
  l=len(stack)
  if (opt>4):
    print("Invalid")
  
  if (opt==1):
    if (l>(top-1)):
      print("Stack is Full..")
    else:  
      ele=input("Enter a element to push: ")
      stack.append(ele)
  elif (opt==2):
    if (l==0):
      print("Stack is empty..")
    else:
      print("Element",stack[-1],"pop from stack")
      stack.pop()
  elif (opt==3):
    if (l==0):
      print("Stack is empty..")
    else:
      print("The stack contain :")
      for i in range(l):
        print(stack[l-1])
        l=l-1
