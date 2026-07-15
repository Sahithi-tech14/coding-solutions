# Problem: Move Zeroes
# Platform: LeetCode
# URL: https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
               if nums[i]==0:
                temp=nums[i]
                nums[j],nums[i]=temp,nums[j]

        return nums