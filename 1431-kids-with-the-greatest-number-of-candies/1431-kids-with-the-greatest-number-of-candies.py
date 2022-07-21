class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        res = []
        #curr = candies[1]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res