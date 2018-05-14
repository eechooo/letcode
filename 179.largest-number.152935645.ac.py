#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (23.60%)
# Total Accepted:    94.1K
# Total Submissions: 398.8K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
# 
# Example 1:
# 
# 
# Input: [10,2]
# Output: "210"
# 
# Example 2:
# 
# 
# Input: [3,30,34,5,9]
# Output: "9534330"
# 
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
#
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x, y: cmp(y + x, x + y))
        
        largest = ''.join(nums)
        
        return largest.lstrip('0') or '0'
    
    
        
