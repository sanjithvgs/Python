''' Add element at Begin in linkedlist
    Delete element at Begin
    Delete element at End
    Delete given element
    print linkedlist 
'''

class Node:
  def __init__(self,data):
    self.data = data
    self.ref = None
class LinkedList:
  def __init__(self):
    self.head = None

  def insert_begin(self,data):
    new_node = Node(data)
    new_node.ref = self.head
    self.head = new_node

  def print_data(self):
    if self.head is None:
      print("List is empty ")
    else:
      n = self.head
      while n is not None:
        print(n.data,end="-->")
        n = n.ref

  def delete_begin(self):
    if self.head is None:
      print("List is empty ")
    else:
      self.head = self.head.ref
  
  def delete_end(self):
    if self.head is None:
      print("List is empty ")
    elif self.head.ref is None:
      self.head = None
    else:
      n = self.head
      while n.ref.ref is not None:
        n=n.ref
      n.ref = None

  def delete_data(self,z):
    if self.head is None:
      print("List is empty")
      return
    if self.head.data == z:
      self.head=self.head.ref
      return
    n = self.head
    while n.ref is not None:
      if n.ref.data == z:
        break
      n=n.ref
    if n.ref is None:
      print("Node not found")
    else:
      n.ref = n.ref.ref

lst = LinkedList()
lst.insert_begin(60)
lst.insert_begin(50)
lst.insert_begin(40)
lst.insert_begin(30)
lst.insert_begin(20)
lst.insert_begin(10)

lst.delete_begin()
lst.delete_end()
lst.delete_data(40)

lst.print_data()