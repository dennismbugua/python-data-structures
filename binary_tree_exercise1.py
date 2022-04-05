#printing binary tree
class Node:
    def __init__ (self, data):
        self.data = data
        self.left = self.right = None

def inorder(temp):
    if not temp:
        return

    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)


def sumOfAllNodes(nodes):
    if nodes is None:
        return 0
    return (nodes.data + sumOfAllNodes(nodes.left) + sumOfAllNodes(nodes.right))

def printNodes(node, level = 0):
    if node is not None:
        printNodes(node.left, level + 1)
        print(' ' * 8 * level + '->', node.data)
        printNodes(node.right, level + 1)

#test code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
root.right.left = Node(6)
printNodes(root)
inorder(root)
f"Inorder is: {print()}"
addition = sumOfAllNodes(root)
print(f"Sum of all nodes is: {addition}")