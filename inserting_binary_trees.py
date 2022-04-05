class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

#Inorder traversal of binary tree
def Inorder(temp):
    if (not temp):
        return
    
    Inorder(temp.left)
    print(temp.key, end=" ")
    Inorder(temp.right)

#funtion to insert element in binary tree
def Insert(temp, key):
    if not temp:
        root = Node(key)
        return
    
    q = []
    q.append(temp)

    #Do level order traversal until we find an empty place
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)


#if __name__ == "__main__":
root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

print(f"Inorder traversal before insertion", end = " ")
Inorder(root)

print(f"Inorder traversal after insertion")
key = 12
Insert(root, key)
Inorder(root)
