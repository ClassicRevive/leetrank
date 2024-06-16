class Node :
    def __init__ (self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val

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

class BinarySearchTree :
    def __init__ ( self ) :
        self.root = None

    def min (self):
        curr = self.root
        while curr.left is not None:
            curr = curr.left

        # we are now at the leftmost (minimum) value
        return curr.val
    
    # inserts x in the tree unless present ;
    # returns pointer to Node with value x
    def insert (self, x) :
        # Part (b)
        node = Node(x)
        if self.root is None:
            self.root = node
            return node

        curr = self.root
        while curr is not None and curr.val != x:
            # traverse left case
            if x < curr.val:
                if curr.left is None:  # leaf position found
                    node.parent = curr
                    curr.left = node
                    return node
                curr = curr.left  # keep traversing

            elif curr.val < x:
                if curr.right is None:  # leaf position found
                    node.parent = curr
                    curr.right = node
                    return node

                curr = curr.right  # keep traversing

def deleteNode(root, key: int):
    # my original over complicated solution
    if root is None:
            return None
    if root.val == key and root.left is None and root.right is None:
        return None
    
    def delete(node, p):
        nonlocal root

        if node:
            print(node)
            print(p)
            # case 1: leaf
            if not node.left and not node.right:
                node = None
            
            # case 2: one child
            elif (node.left and not node.right):
                if node is root:
                    root = root.left
                elif p.left is node:
                    p.left = node.left
                else:
                    p.right = node.left
            elif (node.right and not node.left):
                if node is root:
                    root = root.right
                elif p.left is node:
                    p.left = node.right
                else:
                    p.right = node.right
                
            
            else:  # case 3: two children
                # find smallest child in right subtree
                p = node
                smallest = node.right
                while smallest.left:
                    p = smallest
                    smallest = smallest.left
                
                node.val = smallest.val
                # call delete on smallest. should fall into case 1 or 2 now
                delete(smallest, p)

    # first find the node to delete
    p = None
    curr = root
    while curr:
        if key > curr.val:
            p = curr
            curr = curr.right
        elif key < curr.val:
            p = curr
            curr = curr.left
        else:  # found node, delete it
            delete(curr, p)
            break
    
    return root


# recursive solution
def deleteNode_rec(root, key):
    if not root:
        return None

    def predecessor(node):
        # return the predecessor of current node
        curr = node.left
        while curr.right:
            curr = curr.right
        
        return curr.val
    
    def successor(node):
        curr = node.right
        while curr.left:
            curr = curr.left
        
        return curr.val

    if key < root.val:
        root.left = deleteNode_rec(root.left, key)
    elif key > root.val:
        root.right = deleteNode_rec(root.right, key)
    else:
        # node is a leaf
        if not (root.left or root.right):
            root = None
        elif root.right:
            # node has a right child - replace with successor and delete from successor recursively
            # without parent pointers, this is worst case O(H).
            root.val = successor(root)
            root.right = deleteNode_rec(root.right, root.val)
        else:
            # has left child but not right child, swap with predecessor and float down
            root.val = predecessor(root)
            root.left = deleteNode_rec(root.left, root.val)

    return root



if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(6)
    bst.insert(7)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    
    bst.root.display()
    root = deleteNode_rec(bst.root, 7)
    root.display()
