class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ss = set(nums)
        sd = list(ss)
        print(nums)
        #print(ss)
        #print(sd)
        for i in range(len(sd)):
        #    print(sd[i])
            nums.remove(sd[i])
         #   print(nums)
        ss1 = set(nums)
        r = list(ss.difference(ss1))
        return r[0]