class BinaryTree:
    """
    Creates a binary tree with an optional root node. Supports depth-first printing of values, either pre-order,
    in-order, or post-order
    """

    def __init__(self):
        self.root = None

    def pre_order(self, root=None, nodes=None):
        # Start at the root of our tree
        if root is None:
            root = self.root

        if nodes is None:
            nodes = []

        # Root
        nodes.append(root.value)

        # Left child
        if root.left:
            self.pre_order(root.left, nodes)

        # Right child
        if root.right:
            self.pre_order(root.right, nodes)

        return nodes

    def post_order(self, root=None, nodes=None):
        # Start at the root of our tree
        if root is None:
            root = self.root

        if nodes is None:
            nodes = []

        # Left child
        if root.left:
            self.post_order(root.left, nodes)

        # Right child
        if root.right:
            self.post_order(root.right, nodes)

        # Root
        nodes.append(root.value)

        return nodes

    def in_order(self, root=None, nodes=None):
        # Start at the root of our tree
        if root is None:
            root = self.root

        if nodes is None:
            nodes = []

        # Left child
        if root.left:
            self.in_order(root.left, nodes)

        # Root
        nodes.append(root.value)

        # Right child
        if root.right:
            self.in_order(root.right, nodes)

        return nodes

    def find_maximum_value(self):
        nodes = self.pre_order()
        print(nodes)
        max_val = 0

        for elem in nodes:
            if type(elem) is int or type(elem) is float:
                if elem > max_val:
                    max_val = elem

        return max_val


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

