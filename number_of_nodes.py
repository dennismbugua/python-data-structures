"""
size(tree)
1. If tree is empty then return 0
2. Else
     (a) Get the size of left subtree recursively  i.e., call 
          size( tree->left-subtree)
     (a) Get the size of right subtree recursively  i.e., call 
          size( tree->right-subtree)
     (c) Calculate size of the tree as following:
            tree_size  =  size(left-subtree) + size(right-
                               subtree) + 1
     (d) Return tree_size
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def countNodes(node):
    if node is None:
        return 0
    else:
        return (countNodes(node.left) + countNodes(node.right)) + 1

#test case
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(f"Number of nodes is: {countNodes(root)}")