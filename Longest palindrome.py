class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_={}
        max_=0
        for i in s:
            if i in hash_:
                hash_.pop(i)
                max_+=2
            else:
                hash_[i]=1
        if hash_:
            max_+=1
        return max_
                
        
