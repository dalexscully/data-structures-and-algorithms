import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection


# @pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)


def test_empty_binary_tree():
    tree_a = BinaryTree()
    values = []
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = []

    assert actual == expected


def test_one_empty_binary_tree():
    tree_a = BinaryTree()
    values = []
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = []
    add_values_to_empty_tree(tree_a, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = []

    assert actual == expected


def test_if_tree_have_same_duplicate_values():
    tree_a = BinaryTree()
    values = [150, 100, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    if len(values):
        tree.root = Node(values.pop())
        q = Queue()

        q.enqueue(tree.root)

    else:
        return []

    # print(q.front.value)

    while q.front:
        node = q.dequeue()
        if len(values):
            node.left = Node(values.pop())
            q.enqueue(node.left)
        if len(values):
            node.right = Node(values.pop()) if values else None
            q.enqueue(node.right)
