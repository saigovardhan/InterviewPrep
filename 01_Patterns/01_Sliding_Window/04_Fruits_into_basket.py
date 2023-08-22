"""
Fruits into Baskets (medium)

Problem Statement #
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""

def fruits_into_basket(fruit):
    start, end = 0, 0
    res = 0
    seen = {}

    while end < len(fruit):
        if fruit[end] not in seen:
            seen[fruit[end]] = 0
        seen[fruit[end]] += 1

        while len(seen)>2:
            seen[fruit[start]] -=1
            if seen[fruit[start]] ==0:
                del(seen[fruit[start]])
            
            start+=1
        
        res = max(res, end-start+1)

        end+=1
    
    print(res)


fruits_into_basket(['A', 'B', 'C', 'A', 'C'])
fruits_into_basket(['A', 'B', 'C', 'B', 'B', 'C'])

