# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        L1_list = ""
        L2_list = ""
        Sum = []
        while l1 is not None:
            L1_list = str(l1.val) + L1_list
            l1 = l1.next
        while l2 is not None:
            L2_list = str(l2.val) + L2_list
            l2 = l2.next
        Sum = (int(L1_list) + int(L2_list))
        Sum = str(Sum)
        Sum = list(Sum[::-1])
        out = ListNode()
        current = out
        for num in Sum:
            temp = ListNode()
            temp.val = int(num)
            current.next = temp
            current = current.next
        return out.next
