class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        ans=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return ans
        
