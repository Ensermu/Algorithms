import BST as bst

def update_height(node):
    left_height = node.left.height if node.left else -1
    right_height = node.right.height if node.right else -1 
    node.height = 1 + max(left_height, right_height)
    node.skew = right_height - left_height

class AVL(bst.BST):

    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def insert(self, t):
        node = bst.BST.Tree_Insert(self, t)
        self.maintain(node)

    def maintain(self, node):
        update_height(node)
        self.balance(node)
        if node.parent:
            self.maintain(node.parent)  
            
    def balance(self, node):
        if node.skew == 2:
            if node.right.skew == -1:
                self.right_rotate(node.right)
            self.left_rotate(node)
        if node.skew == -2:
            if node.left.skew == 1:
                self.left_rotate(node.left)
            self.right_rotate(node)
        
    def delete_min(self):
        node, parent = bst.BST.Delete_Min(self)
        self.balance(parent)
        