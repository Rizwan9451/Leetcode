class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l=[]
        for i in range(n):
            l.append([])
            for j in range(n):
                l[i].append(0)
        r1=0
        r2=n-1
        c1=0
        c2=n-1
        s=1
        while(r1<=r2 and c1<=c2):
            for i in range(c1,c2+1):
                l[r1][i]=s
                s+=1
            for i in range(r1+1,r2+1):
                l[i][c2]=s
                s+=1
            if(r2>r1 and c2>c1):
                for i in range(c2-1,c1,-1):
                    l[r2][i]=s
                    s+=1
                for i in range(r2,r1,-1):
                    l[i][c1]=s
                    s+=1
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        return l