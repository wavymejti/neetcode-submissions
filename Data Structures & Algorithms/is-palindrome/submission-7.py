class Solution:
    def isPalindrome(self, s: str) -> bool:
        #variables that i need
        left = 0
        right = len(s) - 1
        lowerS = s.lower()
        while left < right:
            if not lowerS[left].isalpha() and not lowerS[left].isdigit():
                left += 1
                continue
            if not lowerS[right].isalpha() and not lowerS[right].isdigit():
                right -= 1
                continue
            if lowerS[left]== lowerS[right]:
                left += 1
                right -= 1
                continue
            else:
                return False

        return True
