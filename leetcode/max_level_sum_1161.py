def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        # two queues to traverse binary tree by level (BFS)
        curr_level = deque()
        next_level = deque()
        next_level.append(root)
        level = 1
        max_level = 1
        max_sum = float("-inf")

        while next_level:
            curr_level = next_level
            next_level = deque()
            curr_sum = 0

            while curr_level:
                node = curr_level.popleft()
                curr_sum += node.val
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if curr_sum > max_sum:  # update max level
                max_level = level
                max_sum = curr_sum
            
            level += 1

        return max_level
            
