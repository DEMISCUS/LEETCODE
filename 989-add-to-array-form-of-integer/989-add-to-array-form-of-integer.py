class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = 0
        j=0
        no = []
        for i in range(len(num)-1,-1,-1):
            res+= num[i]*(10**j)
            j+=1
        x = res+k
        y=[int(a) for a in str(x)]
        
        
        return y
            
        
        
            