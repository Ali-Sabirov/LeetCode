class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        print(n)
        if n == 0:
            print(n, ' - Exit')
        else:
            #print(n)
            k = nums[0]
            l = 1
            for i in range(1,n):
                if nums[i] > k :
                    k = nums[i]
                    l += 1
                else:
                    nums[i] = '_'
            #print(l, nums)       
            for i in range(1,n-l+1):
                nums.remove('_')
            #print(nums)