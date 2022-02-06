class Solution:
    def firstUniqChar(self, s: str) -> int:
        ret = -1
        if len(s) > 10**5: return ret
        l=list(s)
        abc = list(set(l))
        pos = len(l)
        for i in range(len(abc)):
            if  l.count(abc[i]) == 1:
                j = l.index(abc[i])
                if pos >= j: 
                    pos = ret = j
        return ret