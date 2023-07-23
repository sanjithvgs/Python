class TrieNode:
  def __init__(self):
    self.child={}
    self.isword=False

class Tries:
  def __init__(self):
    self.root=TrieNode()

  def insert(self,word):
    node=self.root
    for char in word:
      if char not in node.child:
        node.child[char]=TrieNode()
        node=node.child[char]
      else:
        node=node.child[char]
    node.isword=True

  def search(self, target):
    node=self.root
    for char in target:
      if char in node.child:
        node=node.child[char]
      else:
        return False
    return node.isword

  
trie=Tries()
arr = ['drink', 'draw', 'drone', 'cat', 'cattle', 'car', 'mango', 'man']
for i in arr:
 trie.insert(i)

trie.search('drink')


# output:
# True