class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode )-> ListNode:
        v=ListNode()
        i=v
        while list1 and list2:
            if list1.val < list2.val:
                i.next=list1
                list1=list1.next
            else:
                i.next=list2
                list2=list2.next
            i=i.next
        if list1:
            i.next=list1
        elif list2:
            i.next=list2
        return v.next  
--------------------------------------------------------------
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
