class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums)==len(set(nums)):
            return 0
        freq={}
        count=0
        for i in nums:
            if i in freq:
                count+=freq[i]
                freq[i]+=1
            else:
                freq[i]=1
        return count
