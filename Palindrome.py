class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:return False
        div=1
        while (x>=10*div):
            div *=10
        while x:
            if(x%10!=x//div):return False
            x=(x%div)//10
            div=div/100
        return True
        
        
*/Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left./*
