# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case: End of branch
        if root is None:
            return 0
        
        # build branch length recursively
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        