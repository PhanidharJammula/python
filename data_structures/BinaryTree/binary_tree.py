class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        """Add child node to the parent node"""
        if data == self.data:
            return # node already exist

        if data < self.data:
            #add data to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #add data to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, value):
        """search for the node in the binary tree"""
        if self.data == value:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def in_order_traversal(self):
        """ In order traversel of the binary tree"""
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        """ Pre order traversel of the binary tree"""

        elements = []

        ##visit base node
        elements.append(self.data)

        ##visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()

        #visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_min(self):
        """find minimum value in  the binary tree"""

        if self.left:
            return self.left.find_min()

        return self.data
        
    def find_max(self):
        """find maximum value in  the binary tree"""

        if self.right:
            return self.right.find_max()

        return self.data

    def calculate_sum(self):
        """find summ of all value in  the binary tree"""

        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self, val):
        """delete a node in the binary tree - 1st way"""

        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def delete1(self, val):
        """delete a node in the binary tree - 2nd way"""

        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self


def build_tree(elements):
    """ Build a binary tree with the given elements"""
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root



if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)

    print("in_order_traversal == %s"%(numbers_tree.in_order_traversal()))
    print("pre_order_traversal == %s"%(numbers_tree.pre_order_traversal()))
    print("post_order_traversal == %s"%(numbers_tree.post_order_traversal()))

    print("value present in the tree %s"%(numbers_tree.search(21)))
    print("minimum value in the tree is %s"%(numbers_tree.find_min()))
    print("maximum value in the tree is %s"%(numbers_tree.find_max()))
    print("sum of all the nodes in the tree is %s"%(numbers_tree.calculate_sum()))

    numbers_tree.delete(20)
    print("After deleting 20 %s"%(numbers_tree.in_order_traversal()))

    numbers_tree.delete1(20)
    print("After deleting1 20 %s"%(numbers_tree.in_order_traversal()))




