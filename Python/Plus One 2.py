class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in range(len(digits)): s += str(digits[i])
        s = str(int(s) + 1)
        d = []
        for i in range(len(s)): d.append(int(s[i]))
        return d