class Node:
    def __init__ (self, data):
        self.data = data
        self.left = self.right = None

#Recursive function to print left view of binary tree
def leftViewUtil(root, level, max_level):
    if root is None:
        return 0

    #if this is the first node of its level
    if max_level[0] < level:
        print(root.data)
        max_level[0] = level

    #Recur for left and right subtree
    leftViewUtil(root.left, level + 1, max_level)
    leftViewUtil(root.right, level + 1, max_level)

#A wrapper over leftViewUtil()
def leftView(root):
    max_level = [0]
    leftViewUtil(root, 1, max_level)

def sum(nodes):
    if nodes is None:
        return
    while nodes:
        sum = int(root.data) + int(root.right) + int(root.left)
        return sum

root = Node(3)
root.left = Node(5)
root.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(9)
leftView(root)
print(sum)