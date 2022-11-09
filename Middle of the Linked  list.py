class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ListNodes=[]
        length=0
        curr=head
        while(curr):
            ListNodes.append(curr)
            length+=1
            curr=curr.next
        return ListNodes[length//2]
----------  --------------------
#Input: head = [1,2,3,4,5]
#Output: [3,4,5]
#Explanation: The middle node of the list is node 3.
