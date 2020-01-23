class Node:
    def __init__(self,key):
        self.root=key
        self.left=None
        self.right=None
preorder=[]
inorder=[]
postorder=[]
tree=Node(1)
tree.left=Node(2)
tree.right=Node(3)
tree.left.left=Node(5)
tree.left.right=Node(10)
tree.left.left.left=Node(20)
tree.left.left.right=Node(30)

tree.right=Node(3)

def preOrder(tree):
    if(tree):
        preorder.append(tree.root)
        preOrder(tree.left)
        preOrder(tree.right)
print(tree)
preOrder(tree)
def postOrder(tree):
    if(tree):
        postOrder(tree.left)
        postOrder(tree.right)
        postorder.append(tree.root)
print(tree)
postOrder(tree)
def inOrder(tree):
    if(tree):
        
        inOrder(tree.left)
        inorder.append(tree.root)
        inOrder(tree.right)
        
print(tree)
inOrder(tree)
print("Inoder :",inorder)
print("Preorder :",preorder)
print("Postoder :",postorder)