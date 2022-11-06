class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=nums[0]
        c=1
        mx=max(nums)+1
        for i in range(len(nums)-1):
            if(n==nums[i+1]):
                c+=1
            else:
                c=1
                n=nums[i+1]
            if(c>2):
                nums[i]=mx
        nums.sort()
        j=len(nums)-1
        while(nums[j]==mx):
            nums.pop()
            j=j-1
        return len(nums)
        
            