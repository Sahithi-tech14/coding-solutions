# Problem: find all dissappeared numbers
# Platform: leet code
# URL:https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
# Difficulty: easy
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        numss=set(nums)
        result=[]
        for i in range(1,n+1):
            if i  not in numss:
                result.append(i)
        return result