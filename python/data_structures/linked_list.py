class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        # Inserts a new node.
        # Args:value to insert
        # returns Nothing
        node = Node(value)

        if self.head is not None:
            node.next = self.head
            # assigned head to be new node
        self.head = node

    def includes(self, value):
        """
             Checks if value is in linked list.
             Args:
                 value (): value to check if in the linked list.
             Returns: Boolean
             """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        """
                Converts linked list to a string.
                Returns: new_str
                """
        new_str = ""
        current = self.head

        while current:
            new_str += f"{{ {current.value} }} -> "
            current = current.next
        new_str += "NULL"
        return new_str


class TargetError:
    pass


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    print(linked_list.includes(4))
    print(linked_list.__str__())
    print(linked_list)

