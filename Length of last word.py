class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip().split(' ')[-1])
        
--------------      -----------------
#Input: s = "Hello World"
#Output: 5
#Explanation: The last word is "World" with length 5.
