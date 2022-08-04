class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        l = 0
        r = len(mat[0])-1
        for i in range(len(mat)):
            if l!= r:
                res+= mat[i][l] + mat[i][r]
            else:
                res+= mat[i][l]
            l+=1
            r-=1
                        
            
        return res