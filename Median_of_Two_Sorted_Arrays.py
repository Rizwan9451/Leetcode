class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # j=0
        # if(len(nums1)>0 and len(nums2)>0):
        #     for i in range(len(nums1)):
        #         if(nums1[i]>nums2[j]):
        #             nums1[i],nums2[j]=nums2[j],nums1[i]
        #             j+=1
        n=len(nums1)+len(nums2)
        l=nums1+nums2
        l.sort()
        if(n%2==0):
            return (l[(n//2)-1]+l[n//2])/2
        else:
            return l[(n//2)]/1
            
                