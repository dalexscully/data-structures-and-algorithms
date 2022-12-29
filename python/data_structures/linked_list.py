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

    def append(self, value):

        # adds a new node with the given value to the end of the list

        current = self.head
        final_node = Node(value)
        if current is None:
            current = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = final_node

    def insert_before(self, search_value, new_value):
        # adds a new node with the given new value immediately before the first node that has the value specified
        if self.head is None:
            raise TargetError("Empty list")

        if not self.includes(search_value):
            raise TargetError('Value not found')

        if self.head.value is search_value:
            node = Node(new_value, self.head)
            self.head = node
        else:
            current = self.head
            while current:
                if current.next.value is search_value:
                    node = Node(new_value, current.next)
                    current.next = node
                    break
                else:
                    current = current.next

    def insert_after(self, search_value, new_value):
        # adds a new node with the given new value immediately after the first node that has the value specified
        if self.head is None:
            raise TargetError("Empty list")
        if not self.includes(search_value):
            raise TargetError("Value not found")

        current = self.head
        while current:
            if current.value is search_value:
                node = Node(new_value, current.next)
                current.next = node
                break
            else:
                current = current.next

    def kth_from_end(self, k):
        """
        Returns the value of the kth node from the tail of the linked list.
        """
        new_list = []
        current = self.head

        if k < 0:
            raise TargetError("k is under range. Input an integer >= 0")

        while current:
            new_list.append(current.value)
            current = current.next

        if abs(-1 - k) > len(new_list):
            raise TargetError("k is out of range")
        else:
            return new_list[- 1 - k]


class TargetError(Exception):
    def __init__(self, message):
        self.message = message


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.append(4)
    print(linked_list.includes(4))
    print(linked_list.__str__())
    print(linked_list)


