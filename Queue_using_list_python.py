# Operations in Queue and Priority_Queue (using List)

queue=[]
opt=0
top=int(input("Enter the size of queue: "))
while (opt!=5):
  opt=int(input("Enter option: 1.Enqueue 2.Requeue 3.Display_Queue 4.Priority_Queue_Requeue 5.Exit : \n"))
  l=len(queue)
  if (opt>5):
    print("Invalid")
  
  if (opt==1):
    if (l>(top-1)):
      print("Queue is Full..")
    else:  
      ele=input("Enter a element to enqueue: ")
      queue.append(ele)
  elif (opt==2):
    if (l==0):
      print("Queue is Empty..")
    else:
      print("Element",queue[0],"requeue from queue")
      z=queue[0]
      queue.remove(z)
  elif (opt==3):
    if (l==0):
      print("Queue is Empty..")   
    else:
      print("The Queue contain :")
      for i in range(l):
        print(queue[i])
  elif (opt==4):
    if (l==0):
      print("Queue is Empty..")
    else:
# In this priority_Queue smallest element is requeue from the queue first 
      queue.sort()
      print("Element",queue[0],"requeue from queue")
      queue.pop(0)
