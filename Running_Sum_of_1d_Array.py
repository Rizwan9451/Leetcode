class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=0
        for i in range(len(nums)):
            l=l+nums[i]
            nums[i]=l
        return nums