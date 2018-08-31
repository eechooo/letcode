#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (38.18%)
# Total Accepted:    912K
# Total Submissions: 2.4M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
# 
# 
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        res = [0] * 2
        for i in range(len(nums)):
            if target - nums[i] in dic:
                res[0] = dic[target - nums[i]]
                res[1] = i
                return res
            else:
                dic[nums[i]] = i
        return res
                
            
        
