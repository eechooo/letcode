#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (36.02%)
# Total Accepted:    121.8K
# Total Submissions: 338.2K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
#
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
#
# 时间复杂度为 O(n * 2 ** n) 空间复杂度 为 O(n * 2 ** n)
#
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]

