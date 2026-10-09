class Solution:
    def isValid(self, s: str) -> bool:
        stringList = list(s)
        stos = []
        odpowiadajce = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for d in stringList:
            if d in odpowiadajce:
                if stos and stos[-1] in odpowiadajce[d]:
                    stos.pop()
                else:
                    return False
            else:
                stos.append(d)
        return True if not stos else False