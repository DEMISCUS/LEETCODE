class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        rep =[]
        c= 1
        for i in range(len(digits)-1,-1,-1):
            n = digits[i]
            n = n+c
            c = n//10
            n = n % 10
            digits[i] = n
        if c==1:
            rep.append(1)
        rep.extend(digits)
#         res+=1
#         while res>0:
#             r= res%10
#             res= res//10
#             rep.append(r)
#         st = 0
#         ed= len(rep)-1
#         while st<ed:
#             rep[st],rep[ed]= rep[ed],rep[st]
#             st+=1
#             ed-=1
        return rep
        