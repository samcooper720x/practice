"""
https://leetcode.com/problems/first-bad-version/
binary search coded in leetcode env to use badversion api
"""
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                right = mid
            
            else:
                left = mid + 1
            
        return left
