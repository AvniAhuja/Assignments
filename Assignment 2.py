#Assignment 2
class Node:
    def __init__(self, data: any):
        self.data = data
        self.next: 'Node' = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def add_to_end(self, data: any) -> None:
        """Add a node with the given data to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self) -> None:
        """Prints all nodes in the list."""
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n: int) -> None:
        """Deletes the nth node (1-based index)."""
        try:
            if n <= 0:
                raise ValueError("Index must be a positive integer.")
            if self.head is None:
                raise IndexError("Cannot delete from an empty list.")

            if n == 1:
                deleted_data = self.head.data
                self.head = self.head.next
                print(f"Deleted node {n} with data '{deleted_data}'")
                return

            current = self.head
            for i in range(n - 2):
                if current.next is None:
                    raise IndexError("Index out of range.")
                current = current.next

            if current.next is None:
                raise IndexError("Index out of range.")

            deleted_data = current.next.data
            current.next = current.next.next
            print(f"Deleted node {n} with data '{deleted_data}'")

        except (IndexError, ValueError) as e:
            print("Error:", e)


# ----------- Sample Test -----------

if __name__ == "__main__":
    ll = LinkedList()

    # Add some elements
    ll.add_to_end("A")
    ll.add_to_end("B")
    ll.add_to_end("C")
    ll.add_to_end("D")

    print("Initial List:")
    ll.print_list()

    # Delete valid node
    ll.delete_nth_node(3)
    print("\nAfter deleting 3rd node:")
    ll.print_list()

    # Delete invalid index
    ll.delete_nth_node(10)

    # Delete with invalid input
    ll.delete_nth_node(0)

    # Delete remaining nodes
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)

    # Try deleting from empty list
    ll.delete_nth_node(1)
