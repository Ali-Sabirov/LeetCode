class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n-1):
            try:
                k = target-nums[i]
                j = nums.index(target-nums[i], i+1, n)
                if j > i: return[i,j]
            except ValueError:
                continue