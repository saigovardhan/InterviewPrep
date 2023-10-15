"""
Kth Smallest Number in a Sorted Matrix (Hard)

Problem Statement #
Given an 
�
∗
�
N∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

Example 1:

Input: Matrix=[
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 
  K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.
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
    Matrix = [
    [2, 6, 8],
    [3, 7, 10],
    [5, 8, 11]]
    K=5
    kth_smallest_in_matrix(Matrix, K)

def kth_smallest_in_matrix(list, k):
    pass