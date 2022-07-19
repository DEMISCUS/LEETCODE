class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        curr=0
        maxW = 0
        for i in range (len(accounts)):
            curr=sum(accounts[i])
            maxW= max(maxW,curr)
        return maxW
    