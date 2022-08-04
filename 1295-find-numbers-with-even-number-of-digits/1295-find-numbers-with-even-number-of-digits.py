class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        a =0
        ans =0
        for i in nums:
            count = i
            while count!=0:
                count=count//10
                a+=1
            if a%2==0:
              ans+=1
            a=0
        
        return ans
            
        