class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
    return list(dfs(root1)) == list(dfs(root2))

def dfs(node):
    # post order traversal where we just store the leaves
    # note the use of yield rather than return for full tree traversal with multiple generator paths.
    if node :            
        if not node.left and not node.right:
            yield node.val
        
        yield from dfs(node.left)
        yield from dfs(node.right)

def test_tree():
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(7)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(7)

    print(leafSimilar(root1, root2))


test_tree()
     

