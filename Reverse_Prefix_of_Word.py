class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l=[]
        m=-1
        for i in range(len(word)):
            if(word[i]!=ch):
                l.append(word[i])
            else:
                l.append(ch)
                m=i
                break
        l.reverse()
        s=""
        for i in range(len(word)):
            if(i<=m):
                s+=l[i]
            else:
                s+=word[i]
        return s
            
        