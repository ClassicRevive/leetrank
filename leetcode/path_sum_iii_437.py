# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict

        def dfs(node, curr_sum: int):
            nonlocal count
            if node:
                curr_sum += node.val
                if curr_sum == targetSum:
                    count += 1
                
                # sum occurs in the middle
                # then add the number of times curr_sum - target 
                # have occured in the current dfs traversal
                count += sum_counts[curr_sum - targetSum]
                
                sum_counts[curr_sum] += 1
                
                dfs(node.left, curr_sum)
                dfs(node.right, curr_sum)
                
                # remove current sum from the hashmap after finishing current branch
                sum_counts[curr_sum] -= 1

        count = 0
        sum_counts = defaultdict(int)
        dfs(root, 0)
        return count
        