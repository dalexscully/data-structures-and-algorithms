from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Creates binary search tree. Add method take a value and adds node with that value. Contains method takes a value
    and returns True if the BinarySearchTree contains that value, otherwise returns False.
    """

    def __init__(self):
        super().__init__()

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while current:
            if value == current.value:
                return
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return
            if value > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)

    def contains(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            if value > current.value:
                current = current.right
        return False
