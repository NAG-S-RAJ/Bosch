# Q4: 
# Complete the PreOrder function, which has 1 parameter: a pointer to the root of a binary 
# tree. It must print the values in the tree's preorder traversal as a single line of space-
# separated values.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def PreOrder(root):
    if root:
        print(root.data, end=' ')     
        PreOrder(root.left)             
        PreOrder(root.right)    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

PreOrder(root)      
