class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        sec=0
        while tickets[k]!=0:
            for i in range(len(tickets)):
                if tickets[i]!=0 and tickets[k]!=0:
                    tickets[i]=tickets[i]-1
                    sec+=1
        return sec    
"""
Input: tickets = [2,3,2], k = 2
Output: 6
Explanation: 
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.
"""
