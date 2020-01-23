class Node:
    def __init__(self,key):
        self.root=key
        self.left=None
        self.right=None

tree=Node(1)
tree.left=Node(2)
tree.right=Node(3)

def preOrder(tree):
    if(tree):
        print(tree.root)
        preOrder(tree.left)
        preOrder(tree.right)
print(tree)
preOrder(tree)
def postOrder(tree):
    if(tree):
        postOrder(tree.left)
        postOrder(tree.right)
        print(tree.root)
print(tree)
postOrder(tree)
def inOrder(tree):
    if(tree):
        
        inOrder(tree.left)
        print(tree.root)
        inOrder(tree.right)
        
print(tree)
inOrder(tree)
