class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt=0
        str1=[]
        for i in s:
            if i=="(" and cnt >0: 
                str1.append(i)
            if i==")" and cnt>1: 
                str1.append(i)
            cnt+=1 if i=="(" else -1    

        return "".join(str1)  
"""
Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
"""
