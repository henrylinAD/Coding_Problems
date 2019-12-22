# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
#
# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?

def reverseList(head):
    dummy = ListNode(float("-inf")) # setting up a dummy value
    while head: 
        dummy.next, head.next, head = head, dummy.next, head.next
    return dummy.next