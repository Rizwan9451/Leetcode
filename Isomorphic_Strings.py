class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        j=-1
        for i in s:
            j+=1
            if(i not in d):
                if(t[j] in d.values()):
                    return False
                d[i]=t[j]
            else:
                if(d[i]!=t[j]):
                    return False
        return True

            
        