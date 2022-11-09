class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        fast = slow = ptr = head
        while fast:
            if not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
