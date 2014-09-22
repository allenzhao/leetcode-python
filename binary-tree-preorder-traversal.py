# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, root, result):
        if root == None:
            return
        result.append(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result)
