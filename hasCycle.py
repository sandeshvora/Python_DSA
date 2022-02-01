# code to detect cycle in Linked list
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self,head:ListNode) -> bool:
        turtle = head
        hare = head
        while(turtle and hare and hare.next):
            hare = hare.next.next
            turtle = turtle.next
            if(turtle == hare):
                return True
        return False

s=Solution()
l1=ListNode(5)
l2=ListNode(6)
l3=ListNode(7)
l4=ListNode(53)
l5=ListNode(52)
l6=ListNode(54)
l1.next =l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l3
ans = s.hasCycle(l1)
print(ans)