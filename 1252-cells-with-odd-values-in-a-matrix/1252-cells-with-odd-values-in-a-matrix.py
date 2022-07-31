class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        count = 0
        ans=[]
        for i in range(m):
            rep=[]
            for i in range(n):
                rep.append(0)
            ans.append(rep)
        #print(ans)
        
        for i in indices:
            row = i[0]
            col = i[1]
            for j in range(m):
                ans[j][col]+=1
            for k in range(n):
                ans[row][k]+=1
        for i in ans:
            for j in i:
                if j%2!=0:
                    count+=1
        
        return count
        
        