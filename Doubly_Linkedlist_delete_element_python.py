'''Creating Doubly Linkedlist
   Add element (at begin)
   Delete element (at begin, at end, delete given element)
   Print Doubly Linkedlist (Forward and Reverse)
'''
class Node:
  def __init__(self,data):
    self.data = data
    self.nref = None
    self.pref = None

class LinkedList:
  def __init__(self):
    self.head = None

  def add_begin(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      new_node.nref = self.head
      self.head.pref = new_node
      self.head = new_node

  def delete_begin(self):
    if self.head is None:
      print("List is empty")
    elif self.head.nref is None:
      self.head = None
    else:
      n = self.head.nref
      n.pref = None
      self.head = n

  def delete_end(self):
    if self.head is None:
      print("List is empty")
    if self.head.nref is None:
      self.head = None
    else:
      n = self.head
      while n is not None:
        a = n
        n = n.nref
      a.pref.nref = None

  def delete_value(self,dlt_data):
    if self.head is None:
      print ("List is empty")
      return
    
    if self.head.nref is None:
      if self.head.data == dlt_data:
        self.head = None
      else:
        print("Element not found")
      return
    
    if self.head.data == dlt_data:
      n = self.head.nref
      self.head = n
      self.head.pref = None
      return

    n = self.head
    while n.nref is not None:
      if n.data == dlt_data:
        break
      n = n.nref
    if n.nref is not None:
      n.nref.pref = n.pref
      n.pref.nref = n.nref
    else :
      if n.data == dlt_data:
        n.pref.nref = None
      else:
        print("Element not found")

  
  def print_data_forward(self):
    if self.head is None:
      print("List is empty")
    else:
      n = self.head
      while n is not None:
         print(n.data,end="-->")
         n = n.nref

  def print_data_back(self):
    if self.head is None:
      print("List is empty")
    else:
      n = self.head
      while n is not None:
         a = n
         n = n.nref
      while a is not None:
         print(a.data,end='-->')
         a = a.pref

lst = LinkedList()    
lst.add_begin(60)
lst.add_begin(50)
lst.add_begin(40)
lst.add_begin(30)
lst.add_begin(20)
lst.add_begin(10)
lst.delete_begin()
lst.delete_value(60)
lst.delete_end()
lst.print_data_forward()
print("\n")
lst.print_data_back()