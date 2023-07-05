class Solution:
    def maxDepth(self, s: str) -> int:
        m,c=0,0
        for i in range(len(s)):
            if s[i]=='(':
                c+=1
                m=max(m,c)
            elif s[i]==')':
                c-=1
        return m 
"""
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.
"""
