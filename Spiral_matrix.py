class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l=[]
        r1=0
        r2=len(matrix)-1
        c1=0
        c2=len(matrix[0])-1
        while(r1<=r2 and c1<=c2):
            for i in range(c1,c2+1):
                l.append(matrix[r1][i])
            for i in range(r1+1,r2+1):
                l.append(matrix[i][c2])
            if(r2>r1 and c2>c1):
                for i in range(c2-1,c1,-1):
                    l.append(matrix[r2][i])
                for i in range(r2,r1,-1):
                    l.append(matrix[i][c1])
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        return l