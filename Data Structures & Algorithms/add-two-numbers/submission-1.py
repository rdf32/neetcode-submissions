# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        numbers_1 = []
        while l1:
            numbers_1.append(l1.val)
            l1 = l1.next
        
        numbers_2 = []
        while l2:
            numbers_2.append(l2.val)
            l2 = l2.next
        
        numbers_1 = numbers_1[::-1]
        numbers_2 = numbers_2[::-1]

        total = str(
            int("".join(map(str, numbers_1))) + 
            int("".join(map(str, numbers_2)))
            )
        output = ListNode(0)
        curr = output
        for i in range(len(total) - 1, -1, -1):
            curr.next = ListNode(total[i])
            curr = curr.next
        return output.next