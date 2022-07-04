class Solution:
    def isValid(self, s: str) -> bool:
        Pairs = { ")":"(", "]":"[", "}":"{" }
        stack = []
        
        for bracket in s:
            if bracket not in Pairs:
                stack.append(bracket)
                continue    
            if not stack or stack[-1] != Pairs[bracket]:
                return False
            stack.pop()
            
        return not stack