#Given a binary tree, delete a node from it by making sure that tree shrinks from the bottom (i.e. the deleted node is replaced by the bottom-most and rightmost node). 
"""Note: We can also replace node’s data that is to be deleted with any node whose left and right child points to NULL but we only use deepest node in order 
to maintain the Balance of a binary tree.

Important Note: This code will not work if the node to be deleted is the deepest node itself because after the function deletDeepest(root, temp) completes execution, 
the key_node gets deleted(as here key_node is equal to temp)and after which replacing key_node‘s data with the deepest node’s data(temp‘s data) throws a runtime error.
To avoid the above error and also to avoid doing BFS twice (1st iteration while searching the rightmost deepest node, and 2nd while deleting the rightmost deepest node), 
we can store parent node while first traversal and after setting rightmost deepest node’s data to the node needed deletion, easily delete the rightmost deepest node."""
class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

def inorder(temp):
    if not temp:
        return

    inorder(temp.left)
    print(temp.key, end=' ')
    inorder(temp.right)
    
    

#function to delete the given deepest node (d_node) in binary tree
def deepestNode(root, d_node):
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)


#function to delete element in binary tree
def deletion(root, key):
    if root == None :
        return None
    if root.left == None and root.right == None:
        if root.key == key :
            return None
        else :
            return root

    key_node = None
    q = []
    q.append(root)
    temp = None
    while len(q):
        temp = q.pop(0)
        if temp.key == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.key
        deepestNode(root, temp)
        key_node.key = x 
    return root



root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.left.right = Node(12)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)
print(f"The tree before deletion: ")
inorder(root)
print()

#print("The sum is: " .format(sum))
key = 11
root = deletion(root, key)
print()
inorder(root)