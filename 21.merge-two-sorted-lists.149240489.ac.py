#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (41.50%)
# Total Accepted:    347.7K
# Total Submissions: 837.8K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        dummy = l3
        while l1 and l2:
            if l1.val > l2.val:
                l3.next = l2
                l2 = l2.next   
            else:
                l3.next = l1
                l1 = l1.next
            l3 = l3.next
            
        if l1:
            l3.next = l1
        
        if l2:
            l3.next = l2
            
        return dummy.next
                
        
                
        
