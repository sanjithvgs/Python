''' Creating Circular linked list
    Add element (at begin)
    print circular linked list
'''
class Node:
  def __init__(self,data):
    self.data = data
    self.nref = None
class c_linkedlist:
  def __init__(self):
    self.head = None

  def add_begin(self,data):
    new_node = Node(data)
    n = self.head     
    new_node.nref = self.head
    if self.head is not None:
        while(n.nref != self.head):
            n = n.nref
        n.nref = new_node
    else:
        new_node.nref = new_node
    self.head = new_node 
      
  def print_data(self):
    n = self.head
    if self.head is not None:
        while(True):
            print(n.data)
            n = n.nref
            if (n == self.head):
                break
    else:
      print("List is empty")
      
cdll = c_linkedlist()
cdll.add_begin(10) 
cdll.add_begin(11) 
cdll.print_data()