class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for s in strs:
            output.append(str(len(s)))
            output.append("#")
            output.append(s)
        return "".join(output)
    def decode(self, s: str) -> List[str]:
        decodedString = []
        i = 0
        while i < len(s):
            hashPlace = s.find("#", i)
            lenght = s[i:hashPlace]
            start = hashPlace + 1
            end = start + int(lenght)
            decodedString.append(s[start:end])
            i = end
        return decodedString
