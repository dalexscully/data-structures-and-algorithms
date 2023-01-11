from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):

    if tree.root is None:
        return []

    queue = Queue()
    queue.enqueue(tree.root)
    result_list = []

    while not queue.is_empty():

        front = queue.dequeue()

        if front.left:
            queue.enqueue(front.left)

        if front.right:
            queue.enqueue(front.right)

        result_list.append(front.value)

    return result_list
