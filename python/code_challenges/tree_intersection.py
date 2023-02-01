from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def tree_intersection(tree1, tree2):
    if not tree1.root or not tree2.root:
        return []

    values = {}
    queue = Queue()

    if tree1.root:
        queue.enqueue(tree1.root)

    while queue.front:
        current = queue.dequeue()

        if current.value not in values:
            values[current.value] = 1

        if current.left:
            queue.enqueue(current.left)

        if current.right:
            queue.enqueue(current.right)

    result = []
    queue_2 = Queue()

    if tree2.root:
        queue_2.enqueue(tree2.root)

    while queue_2.front:
        current = queue_2.dequeue()

        if current.value in values and values[current.value] > 0:
            result.append(current.value)
            values[current.value] -= 1

        if current.left:
            queue_2.enqueue(current.left)

        if current.right:
            queue_2.enqueue(current.right)

    return result
