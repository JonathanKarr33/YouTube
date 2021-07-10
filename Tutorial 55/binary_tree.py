class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
         else:
            self.data = data

   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()

   def preorder_traversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res += self.preorder_traversal(root.left)
         res += self.preorder_traversal(root.right)
      return res
   
root = Node(7)
root.insert(4)
root.insert(10)
root.insert(3)
root.insert(5)
root.insert(8)
root.insert(11)
print(root.preorder_traversal(root))