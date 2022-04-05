class Node:
    def __init__ (self, data):
        self.data = data
        self.left = self.right = None


def maxValue(node):
    if node is None:
        return 0
    
    x = maxValue(node.left)
    y = maxValue(node.right)
    z = node.data
    if x > z:
        z = x
    if y > z:
        z = y
    return z


#test case
root = Node(2)
root.right = Node(4)
root.left = Node(3)
root.left.left = Node(7)
root.right.right = Node(10)
root.right.left = Node(9)
root.left.right = Node(6)
print(f"Max is: {maxValue(root)}")