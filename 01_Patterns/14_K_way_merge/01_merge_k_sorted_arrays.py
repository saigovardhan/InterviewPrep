"""
Merge K Sorted Lists (medium)
We'll cover the following
Problem Statement #
Given an array of 'K' sorted LinkedLists, merge them into one sorted list.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
"""
from heapq import heappush, heappop
class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = next
    def __lt__(self, other):
        return self.value< other.value
    
class MyLinkedList:
    def __init__(self, value) -> None:
        self.head = Node(value)
    
    def add_node(self, value):
        curr = self.head
        if curr is None:
            self.head = Node(value)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next= Node(value)

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(f"{curr.value}", end = "->")
            curr = curr.next
        print()

def main():
    l1 =  MyLinkedList(2)
    l1.add_node(6)
    l1.add_node(8)

    l2 = MyLinkedList(3)
    l2.add_node(6)
    l2.add_node(7)

    l3 = MyLinkedList(1)
    l3.add_node(3)
    l3.add_node(4)
    merge_k_sorted_arrays([l1, l2, l3])


def merge_k_sorted_arrays(lists):
    minHeap = []
    sol = []
    heappush(minHeap, lists[0].head)
    heappush(minHeap, lists[1].head)
    heappush(minHeap, lists[2].head)
    while minHeap:
        poped = heappop(minHeap)
        sol.append(poped.value)
        if poped.next is not None:
            heappush(minHeap, poped.next)
    print(sol)

main()
        




        