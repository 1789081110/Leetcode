class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
         return map(int,str(int("".join(map(str,digits)))+1))
      
--------------        --------------------------
#Input: digits = [9]
#Output: [1,0]
#Explanation: The array represents the integer 9.
#Incrementing by one gives 9 + 1 = 10.
#Thus, the result should be [1,0].

#Input: digits = [1,2,3]
#Output: [1,2,4]
#Explanation: The array represents the integer 123.
#Incrementing by one gives 123 + 1 = 124.
#Thus, the result should be [1,2,4].
