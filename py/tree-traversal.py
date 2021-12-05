class TreeNode(object):
    def __init__(self,val = 0):
        self.val = val
        self.left = None
        self.right = None

#First level
root = TreeNode(1)
#Second level
root.left = TreeNode(2)
root.right = TreeNode(3)

#Third level
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


#Traverse a tree
def preorderTraversal(root):
    if root is None:
        return
    print(root.val)
    preorderTraversal(root.left)
    preorderTraversal(root.right)

#Test
# preorderTraversal(root)

def inorderTraversal(root):
    if root is None:
        return
    
    inorderTraversal(root.left)
    print(root.val)
    inorderTraversal(root.right)

#Test
# inorderTraversal(root)

def postorderTraversal(root):
    if root is None:
        return
    
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.val)

#Test
# postorderTraversal(root)

from collections import deque
def levelorderTraversal(root):
    q = deque()

    q.append(root)

    while(len(q) > 0):
        node =  q.popleft()
        print(node.val)

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

#Test
# levelorderTraversal(root)

