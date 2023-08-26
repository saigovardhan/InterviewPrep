"""
LinkedList Cycle (easy)

Problem Statement #
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
"""


class Node:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next


def linked_list_cycle(head):
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return True

    return False


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print(linked_list_cycle(head))
    head.next.next.next.next = head.next.next
    print(linked_list_cycle(head))


main()
