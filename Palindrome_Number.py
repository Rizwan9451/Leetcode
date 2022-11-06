class Solution:
    def isPalindrome(self, x: int) -> bool:
        l=[]
        s=str(x)
        c=0
        for i in range(len(s)):
            l.append(s[i])
        for i in range(len(l)//2):
            if(l[i]==l[len(l)-i-1]):
                c+=1
        if(c==len(l)//2):
            return True
        else:
            return False