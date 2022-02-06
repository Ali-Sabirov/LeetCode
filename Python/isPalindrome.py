class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        s=s.lower()
        for x in s:
           # print('(', x, ')', x.isalpha())
            if not (x.isalpha() or x.isdigit()):
                s = s.replace(x,'')
        t = s[::-1]
        a = s.replace(t,'')
        
        if len(a) == 0 : return True
        return False