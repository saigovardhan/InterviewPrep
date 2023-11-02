"""
819. Most Common Word
Easy
Topics
Companies : Amazon

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
output : 'a'
"""
from collections import defaultdict
def mostCommonWord(paragraph:str, banned:list[str])->str:
    word_buffer = []
    word = ''
    max_repeated = 0
    banned_words = set(banned)
    sol = ''
    seen = defaultdict(int)
    for i, c in enumerate(paragraph):

        if c.isalnum():
            word_buffer.append(c.lower())
            if i != len(paragraph)-1:
                continue
        
        if len(word_buffer)>0:
            word = ''.join(word_buffer)
            if word not in banned_words:
                    seen[word]+=1
                    if seen[word] > max_repeated:
                        max_repeated = seen[word]
                        sol = word
            word_buffer = []
    print(sol)
    return sol


mostCommonWord("Bob hit ball, hit BALL.", ['hit'])
                        

