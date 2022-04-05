class Node:
    def __init__ (self, data):
        self.data = data
        self.left = self.right = None

"""Give a binary search tree and a number,
inserts a new node with the given number in
the correct place in the tree. Returns the new
root pointer which the caller should then use
(the standard trick to avoid using reference
parameters)."""
def insert(node, data):
    """traverse the node from root to left recursively until left is NULL. The node whose left is NULL is the node with minimum value. """
    #if the tree is empty, return a new single node
    if node is None:
        return (Node(data))
    else:
        #Otherwise recur down the tree
        if data <= node.data:
            node.left = insert(node.left, data)
        else:
            node.right = insert(node.right, data)
        #Return the unchanged node pointer
        return node

"""Given a non-empty binary search tree, 
return the minimum data value found in that
tree. Note that the entire tree does not need
to be searched."""
def minValue(node):
    current = node
    #loop down to find the left most leaf
    while current.left is not None:
        current = current.left
    return current.data


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


def countNodes(node):
    if node is None:
        return 0
    else:
        return (countNodes(node.left) + countNodes(node.right)) + 1


root = None
root = insert(root, 4)
insert(root, 2)
insert(root, 1)
insert(root, 3)
insert(root, 6)
insert(root, 5)
insert(root, 10)
print(f"Min value: {minValue(root)}")
print(f"Max value: {maxValue(root)}")
print(f"No.of nodes: {countNodes(root)}")