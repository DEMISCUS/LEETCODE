class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        count=0
        if ruleKey == "type":
            index = 0
        if ruleKey == "color":
            index = 1
        if ruleKey == "name":
            index = 2
            
        for i in items:
            if i[index]== ruleValue:
                count+=1
        return count