class Solution:
    def reverseString(self, s: List[str]) -> None:
        a = s[::-1]
        for i in range(len(s)): s[i] = a[i]