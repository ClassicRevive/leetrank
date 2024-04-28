# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # traverse the tree, recording the highest number seen so far
        # if the current node is higher than the highest, update highest and the goodnode counter
        # start highest at negative infinity
        highest = float('-inf')
        global count
        
        count = 0
        def dfs(node, highest):
            # traverse the tree and update the count
            global count

            if node:
                if node.val >= highest:
                    count += 1
                    highest = node.val
            
                dfs(node.left, highest)
                dfs(node.right, highest)
        
        dfs(root, highest)
        return count
        