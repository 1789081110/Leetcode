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
-------------------      ----------------------------
#Input: head = [3,2,0,-4], pos = 1
#Output: tail connects to node index 1
#Explanation: There is a cycle in the linked list, where tail connects to the second node.
