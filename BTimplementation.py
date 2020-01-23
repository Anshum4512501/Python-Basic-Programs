class Node:
    def __init__(self,key):
        self.root=key
        self.left=None
        self.right=None

tree=Node(1)
tree.left=Node(2)
tree.right=Node(3)
