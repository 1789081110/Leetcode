class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        ans=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return ans
        
--------- ------------
#Input: head = [1,2,3,4,5]
#Output: [5,4,3,2,1]
