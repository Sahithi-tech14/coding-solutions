# Problem: check if array is sorted and rotated
# Platform: LeetCode
# URL:https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# Difficulty: Easy
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_power=0
        current_power=0
        for i in range(len(nums)):
            if nums[i]==1:
                current_power+=1
                max_power=max(max_power,current_power)
            else:
                current_power=0
        return max_power