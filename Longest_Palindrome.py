class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if(i not in d):
                d[i]=1
            else:
                d[i]+=1
        n=0
        c=0
        for i in d:
            if(d[i]%2==0):
                n+=d[i]
            else:
                n+=(d[i]-1)
                c+=1
        if(c>0):
            return n+1
        return n