from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue


def get_fizz_buzz_val(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


def fizz_buzz_tree(tree):
    new_tree = KaryTree.clone(tree)
    if not new_tree.root:
        return None
    queue = Queue()
    queue.enqueue(new_tree.root)

    while queue.front:
        front = queue.dequeue()
        front.value = get_fizz_buzz_val(front.value)
        for node in front.children:
            queue.enqueue(node)

    return new_tree

