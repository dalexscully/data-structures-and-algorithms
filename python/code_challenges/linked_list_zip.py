from data_structures.linked_list import LinkedList, Node


def zip_lists(a, b):
    current1 = a.head
    current2 = b.head

    if a.head:
        new_ll = LinkedList(a.head)
        current1 = current1.next
        current_new = new_ll.head

    else:
        return b

    while current1 and current2:
        current_new.next = Node(current2.value)
        current2 = current2.next
        current_new = current_new.next

        current_new.next = Node(current1.value)
        current1 = current1.next
        current_new = current_new.next

    while current1:
        current_new.next = Node(current1.value)
        current1 = current1.next
        current_new = current_new.next

    while current2:
        current_new.next = Node(current2.value)
        current2 = current2.next
        current_new = current_new.next

    return new_ll
