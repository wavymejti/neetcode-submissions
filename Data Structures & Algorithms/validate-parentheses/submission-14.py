class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = {
             ")":"(" ,
             "]":"[" ,
             "}":"{" 
        }
        for c in s:
            if c in openings:
                if stack and stack[-1] == openings[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False