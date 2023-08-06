def lPalin(A):
  if A.next==None:
    return 1
  current=A
  count=0
  even_flag=False
  while current:
      count+=1
      current=current.next    
  mid=count//2
  if count%2==0:
      even_flag=True
  #Divide list into 2 parts A and B head
  temp_count=0
  current=A
  B=None
  while True:
      temp_count+=1
      if temp_count==mid and even_flag:
          B=current.next
          current.next=None
          break
      elif temp_count==mid and not even_flag:
          B=current.next.next
          current.next=None
          break
      current=current.next  
  #Reverse B part
  prev=None
  h=B
  rh=h.next
  while h:
      h.next=prev
      prev=h
      h=rh
      if rh:
          rh=rh.next
  #prev is start of B reversed list
  while A and prev:
      if A.val==prev.val:
          A=A.next
          prev=prev.next
      else:
          return 0
  return 1

#Create Linked list start
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        new_node = ListNode(arr[i])
        current.next = new_node
        current = new_node

    return head

#Create Linked list end


A = [1, 2, 2, 1]
head = create_linked_list(A)
print(lPalin(head))

# output:
# 1

# [1,2,2,1] is Palindrome linked list