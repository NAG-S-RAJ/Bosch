class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return BSTNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(node, value):
            if not node:
                return False
            if value == node.value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)
        return _search(self.root, value)

    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        _inorder(self.root)
        return result

    def preorder(self):
        result = []
        def _preorder(node):
            if node:
                result.append(node.value)
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        return result

    def postorder(self):
        result = []
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.value)
        _postorder(self.root)
        return result


bst = BST()
for val in [10, 5, 15, 3, 7]:
    bst.insert(val)

print("BST search 7:", bst.search(7))
print("BST search 8:", bst.search(8))
print("BST inorder traversal:", bst.inorder())
print("BST preorder traversal:", bst.preorder())
print("BST postorder traversal:", bst.postorder())
