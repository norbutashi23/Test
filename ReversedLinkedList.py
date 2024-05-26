# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None  # Initialize a pointer to None. This will eventually become the new tail of the list.
        curr = head  # Initialize another pointer to the head of the list, to start traversing the list.

        # Loop until curr is None, which means we've reached the end of the list.
        while curr:
            next_node = curr.next  # Store the next node temporarily since we're about to change curr.next.
            curr.next = prev  # Reverse the link: point the current node's next pointer to the previous node.
            prev = curr  # Move the prev pointer forward: it now points to the current node.
            curr = next_node  # Move the curr pointer forward: it now points to the next node in the original list.

        # At the end of the loop, curr is None (we've reached the end of the list),
        # and prev is the last node we processed, which is the new head of the reversed list.
        return prev  # Return the new head of the reversed list.
