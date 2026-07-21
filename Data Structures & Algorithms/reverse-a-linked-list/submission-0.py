# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# a->b->c->d->e
# a<-b<-c<-d<-e

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        curr = head
        nextNode = curr.next
        
        while nextNode != None:
            prev = curr
            curr = nextNode
            
            # get next
            nextNode = curr.next

            # if prev is head, remove its next link
            if prev == head:
                prev.next = None
            
            # add link back to prev
            curr.next = prev
        
        return curr