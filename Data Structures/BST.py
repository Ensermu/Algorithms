class BST(object):
    
    def __init__(self):
        self.root = None

    def Tree_Insert(self, x):
        new = BSTnode(x)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                node.size += 1
                if x < node.key:
                    if node.left is None:
                        node.left = new
                        new.parent = node
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return new
    
    def Tree_Search(self, k):
        node = self.root
        while node is not None:
            if k == node.key:
                return node
            if k < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def Tree_Minimum(self):
        node = self.root
        while node.left is not None:
            node = node.left 
        return node.key
    
    def Tree_Minimum1(self, x):
        node = x
        while node.left is not None:
            node = node.left
        return node
    
    def Tree_Maximum(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key
    
    def Delete_Min(self):
        if self.root is None:
            return None, None
        else:
            node = self.root
            while node.left is not None:
                node = node.left
            if node.parent is not None:
                node.parent.left = node.right
            else: 
                self.root = node.right
            if node.right is not None:
                node.right.parent = node.parent
            parent = node.parent
            node.disconnect()
            return node, parent
    
    def Tree_Successor(self, x):
        x = c.Tree_Search(x)
        if x.right is not None:
            return self.Tree_Minimum1(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        if y is None:
            return y
        return y.key
   
    def In_Order_Traversal(self, y):
        if y != None:
            self.Inorder_Tree_Walk(y.left)
            print(y.key)
            self.Inorder_Tree_Walk(y.right) 
            
    def Pre_Order_Traversal(self, node):
        if node != None:
            print(node.key)
            self.Pre_Order_Traversal(node.left)
            self.Pre_Order_Traversal(node.right)
    def Post_Order_Traversal(self, node):
        if node != None:
            self.Post_Order_Traversal(node.left)
            self.Post_Order_Traversal(node.right)
            print(node.key)
    
    def TRANSPLANT(self, u, v):
        if u.parent == None:
            self.root = v
            return 1
        if u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent
    
    def Tree_Delete(self, z):
        z = self.Tree_Search(z)
        if z.left == None and z.right != None:
            self.TRANSPLANT(z,z.right)
        elif z.right == None and z.left != None:
            self.TRANSPLANT(z,z.left)
        elif z.left == None and z.right == None:
            if z.parent.left == z:
                z.parent.left = None
            else:
                z.parent.right = None
        else:
            y = self.Tree_Minimum1(z)
            if y.parent is not z:
                self.TRANSPLANT(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.TRANSPLANT(z, y)
            y.left = z.left
            y.left.parent = y
    
    def Rank(self, k):
        node = self.root
        k = self.Tree_Search(k)
        while node is not None:
            if k.key == node.key:
                if node.left is not None:
                    return node.left.size + 1
                else:
                    return k.rank
            elif k.key > node.key:
                if node.left is None:
                    k.rank += 1
                else:
                    k.rank += node.left.size + 1
                node = node.right
            else:
                node = node.left
        return k.rank 
    
    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])

class BSTnode(object):
    def __init__(self, t):
        self.key = t
        self.size = 1
        self.disconnect()
    def disconnect(self):
        self.left = None
        self.right = None
        self.parent = None
        self.rank = 1
