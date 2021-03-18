''' Creating Doubly Linkedlist
    Add element (at begin, at end, at before given node, at after given node)
    Print Doubly Linkedlist (Forward and Reverse)
'''

class Node:
  def __init__(self,data):
    self.data = data
    self.pref = None
    self.nref = None

class Double_LL:
  def __init__(self):
    self.head = None
  def add_begin(self,data):                  
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      new_node.nref = None
      new_node.pref = None
    else:
      new_node.nref = self.head
      self.head.pref = new_node
      self.head = new_node
      new_node.pref = None
    
  def add_end(self,data):                    
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      n=self.head
      while n.nref is not None:
        n=n.nref
      new_node.pref = n
      n.nref = new_node 

  def add_after_node(self,data,new_data):     
    new_node = Node(new_data)
    if self.head is None:
      print("List is empty")
    else:
      n= self.head
      while n is not None:
        if (n.data == data):
          break
        n = n.nref
      if n is None:
        print("Given element is not found")
      elif n.nref is None:
        n.nref = new_node
        new_node.pref = n
      else:
        new_node.nref = n.nref
        n.nref.pref = new_node
        n.nref = new_node
        new_node.pref = n

  def add_before_node(self,data,new_data):
    new_node = Node(new_data)
    if self.head is None:
      print("List is empty")
    else:
      n = self.head
      while n is not None:
        if (n.data == data):
          break
        n = n.nref
      if n is None:
        print("Given element is not found")  
      elif self.head == n:
        n.pref = new_node
        new_node.nref = self.head
        self.head = new_node
      else:
        n = n.pref
        new_node.nref = n.nref
        n.nref.pref = new_node
        n.nref = new_node
        new_node.pref = n
  
  def print_data_frwd(self):
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
        a=n
        n = n.nref
      while a is not None:
        print(a.data,end="-->")
        a = a.pref

DLL = Double_LL()
DLL.add_begin(50)
DLL.add_begin(40)
DLL.add_begin(30)
DLL.add_begin(20)
DLL.add_begin(10)
DLL.add_end(60)
DLL.add_after_node(60,65)
DLL.add_before_node(30,88)
print("Forward Doubly Linked list: ")
DLL.print_data_frwd()
print("\n")
print("Reverse Doubly Linked list :")
DLL.print_data_back()