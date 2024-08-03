class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Append a new node to the end of the linked list
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    # Print the elements of the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Reverse the linked list
def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

# Sort the linked list using insertion sort
def insertion_sort_linked_list(linked_list):
    sorted_list = LinkedList()
    current = linked_list.head
    while current:
        if not sorted_list.head or current.data < sorted_list.head.data:
            new_node = Node(current.data)
            new_node.next = sorted_list.head
            sorted_list.head = new_node
        else:
            prev = sorted_list.head
            while prev.next and prev.next.data < current.data:
                prev = prev.next
            new_node = Node(current.data)
            new_node.next = prev.next
            prev.next = new_node
        current = current.next
    return sorted_list

# Merge two sorted linked lists
def merge_sorted_linked_lists(list1, list2):
    merged_list = LinkedList()
    current1 = list1.head
    current2 = list2.head
    while current1 and current2:
        if current1.data < current2.data:
            merged_list.append(current1.data)
            current1 = current1.next
        else:
            merged_list.append(current2.data)
            current2 = current2.next
    while current1:
        merged_list.append(current1.data)
        current1 = current1.next
    while current2:
        merged_list.append(current2.data)
        current2 = current2.next
    return merged_list

# Main function
def main():
    # Create the first linked list
    list1 = LinkedList()
    list1.append(3)
    list1.append(1)
    list1.append(4)
    list1.append(2)

    # Create the second linked list
    list2 = LinkedList()
    list2.append(7)
    list2.append(5)
    list2.append(6)

    # Print the first list
    print("The first list:")
    list1.print_list()

    # Reverse the first list
    reverse_linked_list(list1)
    print("Reverse the first list:")
    list1.print_list()

    # Sort the first list
    sorted_list1 = insertion_sort_linked_list(list1)
    print("Sorted first list:")
    sorted_list1.print_list()

    # Print the second list
    print("Second list:")
    list2.print_list()

    # Sort the second list
    sorted_list2 = insertion_sort_linked_list(list2)
    print("Sorted second list:")
    sorted_list2.print_list()

    # Merge the two sorted lists
    merged_list = merge_sorted_linked_lists(sorted_list1, sorted_list2)
    print("The combined sorted list:")
    merged_list.print_list()

if __name__ == "__main__":
    main()