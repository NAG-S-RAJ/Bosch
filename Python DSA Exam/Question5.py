# Q5: 
# Complete the getHeight or height function . It must return the height of a binary tree as an 
# integer. getHeight or height has the following parameter(s): 
# • root: a reference to the root of a binary tree. 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getHeight(root):
    if root is None:
        return -1
    left_height = getHeight(root.left)
    right_height = getHeight(root.right)
    return 1 + max(left_height, right_height)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(getHeight(root))