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
