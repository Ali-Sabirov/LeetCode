class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        n = len(digits)
        x = 0
        for i in range(n): s += str(digits[i])
        x = int(s) + 1
        s = str(x)
        n = len(s)
        d = []
        for i in range(n): d.append(int(s[i]))
        return d  