class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ret = False
        if len(s) != len(t): return ret
        while len(t) > 0:
            x = t[0]
            print('t',t)
            i = t.count(x)
            j = s.count(x)
            print(x, i, 't', t)
            print(x, j, 's', s)
            if i != j or j == 0: 
                return ret
            s = s.replace(x,'',j)
            t = t.replace(x,'',i)
            print('s', s)
  
        if len(s) == len(t) and len(t) == 0: 
            ret = True    
        return ret