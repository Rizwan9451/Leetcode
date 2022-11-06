class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if(len(nums)==0):
            return 0
        else:
            mx=max(nums)+1
            for i in range(len(nums)):
                if(nums[i]==val):
                    nums[i]=mx
            nums.sort()
            j=len(nums)-1
            while(nums[j]==mx):
                nums.pop()
                j-=1
                if(j==-1):
                    break
            return len(nums)