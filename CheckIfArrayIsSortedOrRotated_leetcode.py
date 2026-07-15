# Problem: check if array is sorted and rotated
# Platform: LeetCode
# URL:https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# Difficulty: Easy
from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        count=0
        n=len(nums)
        for i in range(n):
            if nums[i]<nums[(i-1)%n]:
                count+=1
            
        return count<=1
