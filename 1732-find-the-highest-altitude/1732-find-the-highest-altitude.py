class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        res= 0
        alt =[]
        alt.append(0)
        
        for i in gain:
            res = res+i
            alt.append(res)
        print(alt)
        return max(alt)
            
        