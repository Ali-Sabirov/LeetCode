class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        print('n', n)
        x = 0
        for i in range(n):
            x += digits[i]*10**(n-i-1)
        print('x', x)
        x += 1
        print('10**n',10**n)
        if x >= 10**n:
            digits.append('0')
            n = len(digits)
            print('n', n)
        print(x)
        for i in range(n):
            digits[i] = x // (10**(n-i-1))
            x -= digits[i]*(10**(n-i-1))
        #    print(x)
        #print(digits)
        return digits
        