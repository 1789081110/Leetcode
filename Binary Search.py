class Solution:
    def search(self, nums: List[int], n: int) -> int:
        low=0
        high=len(nums)-1  
        mid=0
        while low<=high:
            mid=(high+low)//2
            if nums[mid]<n:
                low=mid+1
            elif nums[mid]>n:
                high=mid-1
            else:
                  return mid
        return -1   
      
      
      # output:Input: nums = [-1,0,3,5,9,12], target = 9 Output: 4  Explanation: 9 exists in nums and its index is 4
