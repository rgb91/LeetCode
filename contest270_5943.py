# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution(object):
#     def deleteMiddle(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         head_backup = head
#         middle = head
#         pre_middle, post_middle = None, None
        
#         if head.next:
#             head = head.next
#             middle = middle.next

#         while True:
#             post_middle = middle.next if middle.next else None
#             pre_middle = middle
#             middle = middle.next

#             if pre_middle:
#                 pre_middle.next = post_middle

#             if head.next is None:
#                 break
#             if head.next.next is None:
#                 break

#             head = head.next.next
        
#         if pre_middle:
#             pre_middle.next = post_middle
        
#         return head_backup


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        
        end = head.next
        pre_middle = head
        while end.next and end.next.next:
            end = end.next.next
            pre_middle = pre_middle.next if pre_middle.next is not None else None
        
        pre_middle.next = pre_middle.next.next
        
        return head

if __name__ == '__main__':
    sln = Solution()
    output = sln.deleteMiddle()
        