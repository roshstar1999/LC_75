class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newNode=head=ListNode()
        
        node1=list1
        node2=list2
        while node1 and node2:
            if node1==list1 and node2==list2:
                flag=1
            
            if node1.val<node2.val:
                newNode.next=ListNode(node1.val)
                node1=node1.next
            else:
                newNode.next=ListNode(node2.val)
                node2=node2.next
                
            if flag==1:
                head=newNode
                flag=0
            newNode=newNode.next
            
        
        if node1!=None:
            newNode.next=node1
        elif node2 !=None:
            newNode.next=node2
      
        return head.next
