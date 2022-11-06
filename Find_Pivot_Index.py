class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l=0
        s=sum(nums)
        for i in range(len(nums)):
            if((s-l-nums[i])==l):
                return i
            l+=nums[i]
        return -1
            
            
            
            