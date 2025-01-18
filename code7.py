# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val  # Value of the current node
#         self.next = next  # Pointer to the next node in the list

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ListNode()  #Head of the list
        s = a  #pointer for traversal
        c = 0  #to store carry if exists

        while l1 and l2:  #loop until either of list is exhausted
            su = (l1.val + l2.val + c)  
            c = su // 10  
            s.next = ListNode(su % 10)
            s = s.next 
            l1 = l1.next  
            l2 = l2.next  

        while l1:  #remaining nodes of list
            su = (l1.val + c)  
            c = su // 10  
            s.next = ListNode(su % 10)  
            l1 = l1.next  
            s = s.next 

        while l2:  #remaining nodes of 2nd list
            su = (l2.val + c) 
            c = su // 10 
            s.next = ListNode(su % 10)  
            l2 = l2.next  
            s = s.next  

        if c:  # when carry exists
            s.next = ListNode(c)  #add a new node with the carry value

        return a.next  #return the head
