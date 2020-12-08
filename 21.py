# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        final_list = ListNode()
        if (l1 is None and l2 is None):
            return None
        p3 = final_list
        while (l1 or l2):
            if (l1 is not None and l2 is not None):
                if (l1.val <= l2.val):
                    p3.val = l1.val
                    l1 = l1.next
                else:
                    p3.val = l2.val
                    l2 = l2.next
            elif (l1 is None):
                p3.val = l2.val
                p3.next = l2.next
                break
            elif (l2 is None):
                p3.val = l1.val
                p3.next = l1.next
                break
            p3.next = ListNode();
            p3 = p3.next
        return final_list
