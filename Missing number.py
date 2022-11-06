#Approach 1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        for num in range(n):
            if num not in nums:
                return num
              
   ------------------------   -------------------------
#Approach 2
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        for j in nums:
            if i==j:
                i+=1
        return i        
----------------------------   -------------------------

#output
#Input: nums = [3,0,1]
#Output: 2
#Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
