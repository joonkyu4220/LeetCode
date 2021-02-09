class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        temp1 = l1
        temp2 = l2
        
        if temp1.val < temp2.val:
            head = temp1
            temp1 = temp1.next
        else:
            head = temp2
            temp2 = temp2.next
        
        
        current = head
        
        while (temp1 and temp2):
            if temp1.val < temp2.val:
                current.next = temp1
                temp1 = temp1.next
                current = current.next
            else:
                current.next = temp2
                temp2 = temp2.next
                current = current.next
        
        if temp1:
            current.next = temp1
            
        if temp2:
            current.next = temp2
        
        return head
