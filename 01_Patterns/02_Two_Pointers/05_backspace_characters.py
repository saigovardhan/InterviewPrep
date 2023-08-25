"""
Comparing Strings containing Backspaces (medium) #
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

Example 1:

Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
Example 2:

Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
Example 3:

Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively.
In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
Example 4:

Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
"""

def backspace(s1, s2):
    p1, p2 = len(s1)-1, len(s2)-1
    while p1 >=0  or p2 >=0:
        if s1[p1] == "#":
            p1 = find_next_non_hash(s1, p1)
        elif s2[p2] =="#":
            p2 = find_next_non_hash(s2, p2)
        elif s1[p1]!=s2[p2]:
            return False
        else:
            p1-=1
            p2-=1
    
    return True
        

def find_next_non_hash(s, p):
    backspaces = 0
    while  p>=0:
        if s[p] == "#":
            backspaces+=1
        elif backspaces>0:
            backspaces-=1
        else:
            break
        p-=1
    return p
        

print(backspace("xy#z", "xzz#"))
print(backspace(s1="xy#z", s2="xyz#"))
print(backspace("abc#b", "#bb#c#b#b"))

