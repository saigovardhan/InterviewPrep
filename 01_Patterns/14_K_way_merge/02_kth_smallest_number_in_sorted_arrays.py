"""
Kth Smallest Number in M Sorted Lists (Medium)

Problem Statement #
Given 'M' sorted arrays, find the K'th smallest number among all the arrays.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged 
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
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
    kth_smallest([l1, l2, l3], 5)

def kth_smallest(list, k):
    minHeap = []
    for l in list:
        heappush(minHeap, l.head)
    t_k = 0
    while minHeap:
        popped = heappop(minHeap)
        t_k+=1
        if k==t_k:
            print(f"the kth smallest is : {popped.value}")
            break
        if popped.next is not None:
            heappush(minHeap, popped.next)
    
main()

