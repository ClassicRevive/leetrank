'''
We have a binary tree and want to implement a breadth-first-search by level.
Here is a 2 queues approach:

list right_most to store answer
two queues: current_level and next_level

- At the start, add root to next_level

While next_level is not empty:
    curr_level = next_level
    empty next level

    load children of all curr_level nodes into next level (left then right)
    Once we're done, the last node to be loaded must be the right most at this level.
    Add this to right_most
'''

from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class BST:
    ''' An implementation of a Binary Search Tree '''
    def __init__(self):
        self.root = None

    def recurse_add(self, ptr, val):
        if ptr is None:  # base case
            return Node(val)
        elif val < ptr.val:  # traverse left
            ptr.left = self.recurse_add(ptr.left, val)
        elif val > ptr.val:  # traverse right
            ptr.right = self.recurse_add(ptr.right, val)
        return ptr  # val is a duplicate

    def add(self, val):
        ''' Add this val to its correct position on the tree '''
        self.root = self.recurse_add(self.root, val)
    
    


def rightSideView(root: Node) -> list:
    # return the values of nodes if we view the tree from the right
    # the right most node at each level is printed
    # use BFS by level
    if root is None:
        return []

    rigthmost = []
    curr_level = deque()
    next_level = deque()
    next_level.append(root)

    while next_level:
        curr_level = next_level
        next_level = deque()

        while curr_level:
            node = curr_level.popleft()
            
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            
        # the last popped node at this level is the rightmost
        rigthmost.append(node.val)
    
    return rigthmost
    

if __name__ == "__main__":
    tree = BST()
    tree.add(10)
    tree.add(3)
    tree.add(8)
    tree.add(6)
    tree.add(12)
    tree.add(9)

    #print(rightSideView(tree.root))


    tree.root.display()
    curr = root
    curr = curr.left
    curr = curr.right
    print()
    tree.root.display()



    

