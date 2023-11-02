"""
Start of LinkedList Cycle (medium)
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
"""


class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

def start_of_linkedlistcycle(head):
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            



def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    # print((head))
    head.next.next.next.next = head.next.next
    # print((head))


main()
