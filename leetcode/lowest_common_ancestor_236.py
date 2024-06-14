# recursive: The concept of backtracking a boolean up the tree is important
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node, visited=set()):
            if not node:  # if we reach the end 
                return False
            
            # 2 recursive paths, also recording if the current node is p or q
            # backtrack the result back up to the LCA
            left = dfs(node.left)
            right = dfs(node.right)

            mid = node is p or node is q

            if mid + left + right >= 2:
                self.ans = node
            
            return mid or left or right

        dfs(root)

        return self.ans

# Non-recursive, using a stack for traversal
# Should be able to interchange between recursive and None. The ideas behind the solutions differ though
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]  # stack for DFS tree traversal
        parent = {root:None}  # store parents for backtracking

        while p not in parent or q not in parent:
            node = stack.pop()  

            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        # now record all ancestors of p
        ancestors = set()
        
        # backtrack from p and add all ancestors to set
        while p:
            ancestors.add(p)
            p = parent[p]
        
        # backtrack q parents until we find a match with p ancestors
        while q:
            if q in ancestors:
                return q
            q = parent[q]