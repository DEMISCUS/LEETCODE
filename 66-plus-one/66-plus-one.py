class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        rep =[]
        for i in digits:
            res = res*10+i
        res+=1
        while res>0:
            r= res%10
            res= res//10
            rep.append(r)
        st = 0
        ed= len(rep)-1
        while st<ed:
            rep[st],rep[ed]= rep[ed],rep[st]
            st+=1
            ed-=1
        return rep
        