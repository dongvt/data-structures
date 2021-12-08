# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        #Helper funtion to get the infotmation in the left subtree
        def leftTraversal(node, res = []):
            if node is None:
                res.append('x')
                return res
            res.append(node.val)
            leftTraversal(node.left,res)
            leftTraversal(node.right,res)
            
            return res
            
        #Helper function to get the information in the right subtree
        def rightTraversal(node, res = []):
            if node is None:
                res.append('x')
                return res
            
            res.append(node.val)
            rightTraversal(node.right,res)
            rightTraversal(node.left,res)
            
            return res
        
        #call the helper function and store both results in lists
        left = leftTraversal(root.left)
        right = rightTraversal(root.right)
        
        #Return the result
        return left == right
        