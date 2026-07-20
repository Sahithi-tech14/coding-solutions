class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count1=0
        count2=0
        for i in range(len(nums)):
            if nums[i]<0:
                count1+=1
            elif nums[i]>0:
                count2+=1
        return max(count1,count2)