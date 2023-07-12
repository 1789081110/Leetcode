class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        ans=money-sum(sorted(prices)[:2])
        if ans>=0:
            return ans
        return money    
      """
      Input: prices = [1,2,2], money = 3
Output: 0
Explanation: Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterward. Thus, we return 0.
      """

